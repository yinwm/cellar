# -*- coding:utf-8 -*-
# cellar.webhandler.page

from cellar.webhandler import BaseHandler

from cellar import settings

class IndexHandler(BaseHandler):

    def get(self):
        self.render('index.tpl')


class ProjectHandler(BaseHandler):

    def get(self):
        cellar_db = settings['mongo_db']
        projects = cellar_db.project.find()
        for p in list(project):
            pass

        self.render('project.html')
