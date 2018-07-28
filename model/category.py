#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Chenbo
@contact: 1126531273@qq.com
@time: 2018/05/15 14:06
"""
from sqlalchemy import Column, Integer, String, DateTime

from flask_app import db


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100))
    user_id = Column(Integer)
    create_time = Column(DateTime)
    update_time = Column(DateTime)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id,
            'create_time': str(self.create_time),
            'update_time': str(self.update_time)
             }
