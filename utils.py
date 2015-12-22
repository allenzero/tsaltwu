#-*- coding: utf-8 -*-
import json
import settings
from tornado.log import app_log

def write_data(stream, template_name, kwargs={}, callback=None):
    '''
    socket write
    '''
    #app_log.info('---------------------------------------------')
    #app_log.info(kwargs)
    kwargs['settings'] = settings
    stream.render(template_name, **kwargs)

class ApiError(Exception):

    def __init__(self, code, msg):

        self.code = code
        self.msg = msg
