import json

from flask import current_app

from status.code import CreateCode


def build_ret(code: CreateCode, total=0, data=None):
    """
    生成请求响应json
    :param code: type(dict) 信息
    :param total: type(int) 数据总数(用于分页)
    :param data: type(list) 数据
    :return: format of json is:
    {
        "data": []
        "total": 0,
        "msg": "",
        "code": 0
    }
    """
    if data is None:
        data = []
    dic = {
        "data": data,
        "total": total,
        "msg": code.msg,
        "code": code.code
    }
    data = json.dumps(dic, ensure_ascii=False)
    dic_json = json.loads(data)
    tran_none_data(dic_json)
    # response_class = Response 封装了相应类对象
    return current_app.response_class(
        (json.dumps(dic_json, ensure_ascii=False)),
        mimetype=current_app.config['JSONIFY_MIMETYPE']
    )


def tran_none_data(dic_json):
    """
    原来的data中可能存在json格式数据，所以在转换为json格式数据后再转回dict做空元素处理
    :param dic_json:
    :return:
    """
    if isinstance(dic_json, dict):
        for key in dic_json:
            if isinstance(dic_json[key], list):
                for li in dic_json[key]:
                    tran_none_data(li)
            elif dic_json[key] is None or dic_json[key] == 'None':
                dic_json[key] = ""
