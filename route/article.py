#!/usr/bin/env python
# encoding: utf-8
"""
@author: Chenbo
@time: 2018/1/9 14:24
"""
import json
from logging import exception

from flask import request

from flask_app import app

from service.article import list_article, article_infos
from status import code
from util.common import build_ret


@app.route("/posts", methods=['GET'])
def article_list():
    parameter = request.args.to_dict()
    page = parameter.get('page') if parameter.get('page') else 1

    articles, total = list_article(page=page)
    return build_ret(code=code.CODE_SUCCESS, data=articles, total=total)


@app.route("/post", methods=['GET'])
def article_information():
    parameter = request.args.to_dict()
    ids = parameter.get("id")
    if ids is None or ids == "":
        raise Exception("id不能为空！", ids)
    data = article_infos(ida=ids)
    print(data)

    return build_ret(code=code.CODE_SUCCESS, data=data)


@app.route("/a", methods=['GET'])
def results():
    # print("测试一下链接")
    return "desperate"