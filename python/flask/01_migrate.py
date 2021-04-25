#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)


class Config(object):
    """配置参数"""
    DEBUG = True

    SQLALCHEMY_DATABASE_URI= 'mysql+pymysql://root:aa1231231@127.0.0.1:3306/author_book_02'

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = '!@#$%^&*()'


app.config.from_object(Config)
db = SQLAlchemy(app)

# 创建flask脚本管理工具
manager = Manager(app)

# 创建数据库迁移管理工具对象
Migrate(app, db)

# 向manager对象中添加数据库的操作命令
manager.add_command('db', MigrateCommand)


class Author(db.Model):
    __tablename__ = "tbl_authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 模型类关联，表中没有该字段，依赖ForeignKey
    # backref在关联的模型类中增加相对应的属性
    books = db.relationship('Book', backref="author")


class Book(db.Model):
    __tablename__ = 'tbl_books'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 表中外键
    author_id = db.Column(db.Integer, db.ForeignKey('tbl_authors.id'))


def without_migrate():
    # 清理数据库里所有的数据
    db.drop_all()

    # 创建所有的表
    db.create_all()

    # 创建对象
    author1 = Author("admin")
    # session 会话
    db.session.add(author1)
    db.commit()

    # db.session.add_all([])


if __name__ == '__main__':
    manager.run()


