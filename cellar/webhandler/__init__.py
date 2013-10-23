# -*- coding:utf-8 -*-
# cellar.webhandler

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    pass

def build_route():
    from .page import IndexHandler
    return [
        (r'/', IndexHandler),
        ]


