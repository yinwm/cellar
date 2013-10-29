# -*- coding:utf-8 -*-
# cellar.webhandler

import tornado.web
from tornado.escape import json_encode

def web_ret(err_code=0, err_msg=''):
    d = { 'err_code': err_code,
          'err_msg': err_msg,
          'result': {}
          }
    return d


def jsonify(func):
    def wrapper(*args, **kwargs):
        handler = args[0]
        v = func(*args, **kwargs)
        handler.set_header("Content-Type", "application/json")
        handler.write(json_encode(v))

    return wrapper
        

class BaseHandler(tornado.web.RequestHandler):
    pass

def build_route():
    from .page import IndexHandler
    from .store import UploadHandler, GetFileHandler
    return [
        (r'/', IndexHandler),
        (r'/([\w]+)/upload/$', UploadHandler),
        (r'/([\w]+)/([\w-]+)/?$', GetFileHandler),
        ]


