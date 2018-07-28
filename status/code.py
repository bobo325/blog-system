"""
@version: 1.0
@author: Chenbo
@contact: 1126531273@qq.com
@time: 2018/05/15 14:06
"""

CODE_MAPPING = []


class Code(object):
    def __init__(self, code, msg, err_code=0):
        self.code = code
        self.msg = msg
        self.err_code = err_code
        CODE_MAPPING.append(self.__dict__)


class CreateCode(Code):

    def __init__(self, code, msg, err_code=0):
        Code.__init__(self, code=code, msg=msg, err_code=err_code)
        pass

    def __call__(self, *args, **kwargs):
        return self.__dict__


CODE_SUCCESS = Code(0, "操作成功")
CODE_SYS_ERROR = Code(9999, "系统错误")
CODE_SYS_PAGE_NOT_FOUND = Code(9998, "页面或资源不存在")
CODE_SYS_INVALID_REQUEST = Code(9997, "请求错误")
CODE_SYS_NOT_PERMISSION = Code(9996, "没有权限")

CODE_TOKEN_EXPIRED = Code(1001, "会话超时")
CODE_TOKEN_INVALID = Code(1002, "用户凭证校验失败")

CODE_USER_INVALID__PASSWORD = Code(1100, "密码错误")
CODE_USER_INVALID_OLD_PASSWORD = Code(1101, "原密码错误")
CODE_USER_NOT_EXISTS = Code(1102, "用户不存在")
CODE_USER_HAS_EXISTS = Code(1103, "用户名已经存在")

CODE_ARTICLE_NOT_EXISTS = Code(1102, "文章已失效")