# -*- coding:utf-8 -*-
# mainweb

import os
import datetime

import tornado.ioloop
import tornado.web

from pymongo import MongoClient

from cellar import build_settings

if __name__ == "__main__":

    from tornado.options import define, options
    define("port", default=38080, help="run on the given port", type=int)
    options.parse_command_line()

    settings = build_settings('app.yaml')

    conn = MongoClient(settings['mongo']['host'], settings['mongo']['port'])

    settings.update(
        mongo_conn = conn,
        mongo_db   = conn[settings['mongo']['db']],
        template_path = os.path.join(os.path.dirname(__file__), "templates"),
        )

    from cellar.webhandler import build_route as main_build_route
    
    app = tornado.web.Application(
        main_build_route(),
        **settings)

    app.listen(options.port)
    print '[', datetime.datetime.now(), '] Started on port', options.port
    tornado.ioloop.IOLoop.instance().start()

