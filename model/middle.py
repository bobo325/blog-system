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


class Middle(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    article_id = Column(Integer)
    label_id = Column(Integer)

    def to_json(self):
        return {
            'id': self.id,
            'article_id': self.article_id,
            'label_id': self.label_id
             }
