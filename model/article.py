#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Chenbo
@contact: 1126531273@qq.com
@time: 2018/05/15 14:06
"""

from sqlalchemy import Column, Integer, String, Text, DateTime

from flask_app import db


class Article(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=100))
    user_id = Column(Integer)
    md_value = Column(Text)
    html_value = Column(Text)
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    category_name = Column(String(length=100))

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'user_id': self.user_id,
            'md_value': self.md_value,
            'html_value': self.html_value,
            'create_time': str(self.create_time),
            'update_time': str(self.update_time),
            "category_name": self.category_name
             }
