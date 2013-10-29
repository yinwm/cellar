# -*- coding:utf-8 -*-
# cellar.webhandler.store

import datetime
from uuid import uuid1

from tornado.web import addslash

import gridfs

from cellar import settings, errcode

from cellar.webhandler import BaseHandler, web_ret, jsonify

class UploadHandler(BaseHandler):

    @addslash
    def get(self, proj):
        data = {
            'proj': proj
            }
        self.render('upload.tpl', **data)
        

    @addslash
    @jsonify
    def post(self, proj):
        file_info = None
        if 'file' in self.request.files:
            l = self.request.files['file']
            if len(l) > 0:
                file_info = l[0]

        ret = web_ret()
        if not file_info:
            ret['err_code'] = errcode.UPLOAD_NO_FILE
            return ret

        print type(file_info)

        '''
        - filename
        - body
        - content_type
        '''
        
        db = settings['mongo_conn'][proj]
        fs = gridfs.GridFS(db)
        _uuid = str(uuid1())
        info = {
            '_id': _uuid,
            'uuid': _uuid,
            'created_at': datetime.datetime.now(),
            'filename': file_info['filename'],
            'content_type': file_info['content_type'],
            }
        fid = fs.put(file_info['body'], **info)

        ret['result']['uuid'] = fid
        return ret
        

class GetFileHandler(BaseHandler):

    @addslash
    def get(self, proj, uuid):
        db = settings['mongo_conn'][proj]
        fs = gridfs.GridFS(db)
        f = fs.get(uuid)

        self.set_header("Content-Type", f.content_type)
        self.write(f.read())
        
        
