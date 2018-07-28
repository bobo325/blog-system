#!/usr/bin/env python
# encoding: utf-8
"""
@author: Chenbo
@time: 2018/1/9 14:24
"""

from flask import request

from flask_app import app
from flask_app.app import db
from datetime import datetime

from service.user import login, register
from util.common import build_ret


@app.route("/user/login", methods=['POST'])
def user_login():
    # id 自增导致问题如何解决的
    username = request.form["username"]
    password = request.form["password"]
    # print("username", username)
    result_code = login(username, password)
    return build_ret(result_code)


@app.route("/user/register", methods=['POST'])
def user_register():
    username = request.form["username"]
    password = request.form["password"]
    gender = request.form["gender"]
    tel = request.form["tel"]
    email = request.form["email"]
    nickname = request.form["nickname"]
    result_code = register(username=username, password=password, gender=gender, tel=tel,
                           email=email, nickname=nickname)
    return build_ret(result_code)
