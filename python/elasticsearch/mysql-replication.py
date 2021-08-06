#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/5 16:34
# @Author  : hzy
# @File    : sync_sql_to_es.py
# @Software: PyCharm


import pymysql
import requests
import datetime
from retrying import retry
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import (
    DeleteRowsEvent,
    UpdateRowsEvent,
    WriteRowsEvent
)
import logging

logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO, format="%(asctime)s;%(levelname)s;%(message)s")
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(level=logging.INFO)

MYSQL_SETTINGS = {'host': '10.0.0.22', 'port': 3306, 'user': 'root', 'passwd': 'rootPassw0rd2020'}
# MYSQL_SETTINGS = {'host': '10.10.84.204', 'port': 3306, 'user': 'root', 'passwd': 'rootPassw0rd2020'}
es = Elasticsearch("elasticsearch.kube-system:9200")
# es = Elasticsearch("http://es.aidigger.com/")
es_session = requests.Session()
es_session.trust_env = False
index_name = 'bees_articles_stcn'
sql = """SELECT * FROM user_article_model"""
num = 0


class ConnectFactory:
    @classmethod
    def connect(cls,
                host='10.0.0.22',
                port=3306,
                user='root',
                passwd='rootPassw0rd2020',
                database='bee',
                cursorclass=pymysql.cursors.DictCursor,
                charset='utf8mb4'):
        return pymysql.connect(host=host,
                               port=port,
                               user=user,
                               password=passwd,
                               database=database,
                               cursorclass=cursorclass,
                               charset=charset)

    @classmethod
    def get_connect(cls, db='bee'):
        return cls.connect(**MYSQL_SETTINGS, database=db)


def str_datetime(x: datetime.datetime):
    if isinstance(x, datetime.datetime):
        return datetime.datetime.strftime(x, "%Y-%m-%d %H:%M:%S")
    return x


field_meta = {
    'id': int,
    'type': str,
    'is_deleted': bool,
    'user_id': int,
    'team_id': int,
    'folder_id': int,
    'title': str,
    'cover_image': str,
    'contents': str,
    'topic': str,
    'comments': str,
    'suggests': str,
    'meta_info': str,
    'check_status': int,
    'publish_status': int,
    'author': str,
    'create_time': str_datetime,
    'update_time': str_datetime,
    'assign_time': str_datetime,
    'check_time': str_datetime,
    'last_publish_time': str_datetime,
    'last_operator': int,
    'article_category': str,
    'article_type': str,
    'create_user_id': int,
    'trace_id': str,
    # 'process_id': int,
    # 'from_kafka_offset': int
}


def convert_data(values: dict, timestamp=None) -> dict:
    # 根据field_meta转换数据格式
    res = {}
    for key, value in values.items():
        if field_meta.get(key, None):
            if value is None:
                res[key] = value
            else:
                res[key] = field_meta[key](value)
    # values['from_kafka_offset'] = timestamp or int(datetime.datetime.now().timestamp())
    return res


@retry(stop_max_attempt_number=3, wait_fixed=100)
def bulk_write_to_es(op):
    global num
    num += 1
    logger.info(f'write_to_es: {num}')
    try:
        bulk(es, op)
    except Exception as e:
        logger.error(e)


def write_all_articles_to_es():
    connect = ConnectFactory.get_connect(db='bee')
    with connect.cursor() as cursor:
        op = []
        cursor.execute(sql)
        for data in cursor:
            doc = {
                '_op_type': 'update',
                '_index': index_name,
                '_type': 'doc',
                '_id': data['id'],
                'doc': convert_data(data),
                'doc_as_upsert': True
            }
            op.append(doc)
            if len(op) >= 100:
                bulk_write_to_es(op)
                op = []
        if len(op) > 0:
            bulk_write_to_es(op)
    connect.close()


def delete(row: dict, timestamp):
    data = convert_data(row['values'], timestamp)
    # print(data)
    return dict(index=index_name,
                doc_type='doc',
                id=row['values']['id'])


def update(row: dict, timestamp):
    #     data = diff_value(row['before_values'],row['after_values'])
    data = convert_data(row['after_values'], timestamp)
    # print(data)
    return dict(index=index_name,
                doc_type='doc',
                body=data,
                id=row['after_values']['id'])


def insert(row: dict, timestamp):
    data = convert_data(row['values'], timestamp)
    # print(data)
    return dict(index=index_name,
                doc_type='doc',
                body=data,
                id=row['values']['id'])


event_func_map = {
    DeleteRowsEvent: delete,
    UpdateRowsEvent: update,
    WriteRowsEvent: insert
}

func_es_map = {
    delete: es.delete,
    update: es.index,
    insert: es.index
}


@retry(stop_max_attempt_number=3, wait_fixed=100)
def write_to_es(func, data):
    try:
        func_es_map[func](**data)
    except Exception as e:
        logger.error(e)


def sync_sql_to_es():
    stream = BinLogStreamReader(
        connection_settings=MYSQL_SETTINGS,
        only_events=[DeleteRowsEvent, WriteRowsEvent, UpdateRowsEvent],
        only_schemas=['bee'],
        only_tables=['user_article_model'],
        server_id=83,
        skip_to_timestamp=1628074154,
        blocking=True
    )

    for binlogevent in stream:
        prefix = "%s:%s:" % (binlogevent.schema, binlogevent.table)
        logger.info(f'SYNC {prefix.upper()}')
        timestamp = binlogevent.timestamp
        func = event_func_map[type(binlogevent)]
        for row in binlogevent.rows:
            data = func(row, timestamp)
            logger.info(f'timestamp[{timestamp}]<--->{func.__name__.upper()}<--->article[{data["id"]}]')
            # print(data)
            write_to_es(func, data)
    stream.close()


if __name__ == '__main__':
    sync_sql_to_es()

