#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   auto_map.py
@Time    :   2023/4/11 16:13 
@Author  :   zhenyu.hu
@Desc    :   <awaiting description>
"""
import types
import weakref
from collections import namedtuple
from dataclasses import dataclass, Field
from typing import Dict, Any, List

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, relationship, joinedload

metadata = MetaData()
Base = automap_base()
Session = sessionmaker()


class NotFound(Exception):
    pass


@dataclass(init=False)
class Model(object):
    table_name: str
    source: str
    columns: Dict[str, Any]
    primary_keys: List[str]

    def __init__(self, table_name, source, columns, primary_keys):
        assert table_name is not None, ValueError
        assert source in ["table", "class"], ValueError
        self.table_name = table_name
        self.source = source
        self.columns = columns
        self.primary_keys = primary_keys


class Cached(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls.__cache = weakref.WeakValueDictionary()

    def __call__(cls, *args):
        if args not in cls.__cache:
            obj = super().__call__(*args)
            cls.__cache[args] = obj
        return cls.__cache[args]


class DBMeta(type):

    def __new__(mcs, name: str, bases: tuple, attrs: dict):
        model_meta = {}
        for k, v in attrs.copy().items():  # attrs unordered
            if isinstance(v, Model):
                model_meta[k] = v
                del attrs[k]
        attrs['model_meta'] = model_meta
        return type.__new__(mcs, name, bases, attrs)

    def __call__(cls, *args, engine, **kwargs):
        metadata.reflect(engine)
        instance = super().__call__(*args, engine=engine, **kwargs)
        cls.__init_models(instance, Base, metadata)
        Base.prepare(engine)
        return instance

    def __init_models(self, instance, base, metadata):
        for name, filed in instance.model_meta.items():
            if filed.source == "class":
                cls_dict = self.get_classes_dict(filed)
            else:
                cls_dict = self.get_tables_dict(filed, metadata)

            new_model = types.new_class(name, (base,), {}, lambda ns: ns.update(cls_dict))
            new_model.__module__ = __name__
            setattr(instance, name, new_model)

    @staticmethod
    def convert_primary_keys(table, primary_keys):
        primary_key = []
        for key in primary_keys:
            prop = getattr(table.c, key)
            if prop is None:
                raise NotFound(f"{key} not in {table}")
            primary_key.append(prop)
        return primary_key

    @staticmethod
    def get_classes_dict(filed, *args, **kwargs):
        return {
            "__tablename__": filed.table_name,
            **filed.columns
        }

    def get_tables_dict(self, filed, metadata):
        """
        create no primary key tables
        """
        if not filed.primary_keys:
            raise NotFound(f"{filed.table_name} not find primary_keys")
        if filed.table_name not in metadata.tables:
            raise NotFound(f"{filed.table_name} not in tables")
        table = metadata.tables[filed.table_name]
        primary_key = self.convert_primary_keys(table, filed.primary_keys)
        return {
            "__table__": table,
            "__mapper_args__": {
                "primary_key": primary_key
            }
        }


class DB(metaclass=DBMeta):
    Image = Model("CLAIM_IMAGE_INFO", "table", None, ["TASK_ID", "IMAGE_ID"])
    Code = Model("CLAIM_INSURANCE_TYPE_INFO", "table", None, ["TASK_ID", "CODE"])
    Task = Model(
        "CLAIM_TASK_INFO",
        "class",
        {
            "images": relationship(
                "Image",
                primaryjoin="Task.TASK_ID == foreign(Image.TASK_ID)"
            ),
            "codes": relationship(
                "Code",
                primaryjoin="Task.TASK_ID == foreign(Code.TASK_ID)"
            )
        },
        None
    )

    def __init__(self, *args, engine, **kwargs):
        self.engine = engine


class Handler(metaclass=Cached):
    DBClass = DB

    def __init__(self, url):
        self.engine = create_engine(
            url,
            pool_recycle=60 * 30,
            pool_pre_ping=True
        )
        self.db = DB(engine=self.engine)
        Session.configure(bind=self.engine)

    def query(self, count=1):
        with Session() as session:
            query = session.query(self.db.Task).join(self.db.Image, self.db.Image.TASK_ID == self.db.Task.TASK_ID)
            query = query.filter(self.db.Task.STATUS == 0)
            query = query.options(joinedload(self.db.Task.images), joinedload(self.db.Task.codes))
            # if start_time and end_time:
            #     query = query.filter(self.Task.END_TIME.between(start_time, end_time))
            if count:
                query = query.limit(count)
            return [task.TASK_ID for task in query]


if __name__ == '__main__':
    handler = Handler("mysql+pymysql://danube-test:danube-test@172.18.4.249:3306/DANUBE_II_TEST?charset=utf8mb4")
    print(handler.query())
