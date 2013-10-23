# -*- coding:utf-8 -*-
# cellar.webhandler.page

from cellar.webhandler import BaseHandler

class IndexHandler(BaseHandler):

    def get(self):
        self.render('index.tpl')


