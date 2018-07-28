#!/usr/bin/env python
# encoding: utf-8
'''
@version: 1.0
@author: Chenbo
@contact:
@time:
'''
import status
from flask_app.app import db

from model.user import User
from status import code


def login(username, password):
    login_user = User.query.filter(User.username == username)
    if not login_user:
        return code.CODE_USER_NOT_EXISTS
    for every in login_user.all():
        if every.password == password:
            print("登录成功!")
            return code.CODE_SUCCESS
        else:
            pass
    return code.CODE_USER_INVALID__PASSWORD


def register(username, password, gender, tel, email, nickname):
    register_user = User.query.filter(User.username == username)
    if register_user:
        return code.CODE_USER_HAS_EXISTS
    new_user = User()
    new_user.username = username
    new_user.password = password
    new_user.gender = gender
    new_user.tel = tel
    new_user.email = email
    new_user.nickname = nickname
    db.session.add(new_user)
    db.session.commit()