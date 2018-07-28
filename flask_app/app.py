#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Chenbo
@contact: 1126531273@qq.com
@time: 2018/05/15 14:06
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# sqlalchemy setup
from config.config import db_config

app = Flask(__name__)  # type: Flask

app.config["SQLALCHEMY_DATABASE_URI"] = db_config["url"]
# 如果设置成True(默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
# 这需要额外的内存， 如果不必要的可以禁用它。如果你不显示的调用它，在最新版的运行环境下，
# 会显示警告。
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
