#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Chenbo
@contact: 1126531273@qq.com
@time: 2018/05/15 14:06
"""
from sqlalchemy import Column, Integer, String

from flask_app import db


class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(length=100))
    password = Column(String(length=100))
    gender = Column(Integer)
    tel = Column(String(length=100))
    email = Column(Integer)
    nickname = Column(String(length=100))

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.name,
            'gender': self.gender,
            'tel': self.tel,
            'email': self.email,
            'nickname': self.nickname
             }
