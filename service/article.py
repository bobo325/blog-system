#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/1/9 14:24
"""
from sqlalchemy import text

from model.article import Article
from model.category import Category
from model.user import User
from status import code


def list_article(page=1):
    article_list = Article.query.order_by(Article.create_time.desc())
    offset = (int(page) - 1) * 6 if page else 0
    limits = 6
    total = article_list.count() if article_list else 0
    articles = []
    for every in article_list.offset(offset).limit(limits).all():
        # 获取nickname
        user_id = every.user_id
        user = User.query.filter(User.id == user_id).one_or_none()
        if not user:
            nickname = ""
            category_name = ""
        else:
            nickname = user.nickname
            category_name = user.category_name
        idz = every.id
        title = every.title
        html_value = every.html_value
        create_time = str(every.create_time)
        article = {
            "id": idz,
            "title": title,
            "html_value": html_value,
            "category_name": category_name,
            "create_time": create_time,
            "nickname": nickname
        }
        articles.append(article)
    return articles, total


def article_infos(ida):
    article_detail = Article.query.filter(Article.id == ida).one_or_none()
    if not article_detail:
        return code.CODE_ARTICLE_NOT_EXISTS
    # 获取昵称
    user_id = article_detail.user_id
    user = User.query.filter(User.id == user_id).one_or_none()
    if user:
        nickname = user.nickname
    else:
        nickname = ""
    category_name = article_detail.category_name
    idx = article_detail.id
    title = article_detail.title
    html_value = article_detail.html_value
    print("html_value的类型", type(html_value))
    create_time = article_detail.create_time
    article = {
        "id": idx,
        "title": title,
        "html_value": html_value,
        "category_name": category_name,
        "create_time": create_time.strftime("%Y-%m-%d %H:%M:%S"),
        "nickname": nickname
    }
    #print(article)
    return article


def article_category(idb, page=1):
    offset = (int(page) - 1) * 6 if page else 0
    limits = 6
    category = Category.query.filter(Category.id == idb)
    categoryname = category.name
    articles = Article.query.filter(Article.category_name == categoryname).order_by(Article.create_time.desc())
    total = articles.count() if articles else 0
    data = []
    for every in articles.offset(offset).limit(limits).all():
        # 获取nickname

        user_id = every.user_id
        user = User.query.filter(User.id == user_id).one_or_none()
        if not user:
            nickname = ""
        else:
            nickname = user.nickname
        category_name = user.category_name
        idz = every.id
        title = every.title
        html_value = every.html_value
        create_time = every.create_time
        article = {
            "id": idz,
            "title": title,
            "html_value": html_value,
            "category_name": category_name,
            "create_time": create_time,
            "nickname": nickname
        }
        data.append(article)
    return data, total
