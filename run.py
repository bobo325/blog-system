"""
@version: 1.0
@author: Chenbo
@contact: 1126531273@qq.com
@time: 2018/05/15 14:06
"""
from flask_cors import CORS

from config import web_config
from flask_app import app

if __name__ == '__main__':
    # 跨域分享 cross origin resource sharing
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})    条件性访问
    CORS(app)
    host = web_config["ip"]
    port = web_config["port"]
    is_debug = web_config['debug']
    if is_debug:
        app.run(host=host, port=port, debug=True)
    else:
        app.run(host=host, port=port)