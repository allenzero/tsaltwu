#-*- coding: utf-8 -*-
import os, sys, traceback
import settings
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.gen
from tornado.log import app_log
import json, time
from utils import write_data, ApiError
from tornado.httpclient import AsyncHTTPClient, HTTPRequest

pid = os.getpid()

class BaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        app_log.info('-----------------get current user---------------')
        app_log.info(self.get_secure_cookie('user'))
        return self.get_secure_cookie('user')

    def write_error(self,status_code,**kwargs):
        app_log.info('--------------write error------------')
        if status_code == 404:
            self.render('error/404.html')
        elif status_code == 500:
            self.render('error/500.html')
        else:
            super(BaseHandler, self).write_error(status_code,**kwargs)

class IndexHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        write_data(self, 'index.html', {
            })

class LeftHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        write_data(self, 'left.html', {})

class MainHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        write_data(self, 'main.html', {})

class LoginHandler(BaseHandler):

    def post(self):
        if self.get_current_user():
            raise tornado.web.HTTPError(403)
        username = self.get_argument('form-username')
        password = self.get_argument('form-password')
        login_error = None
        #login_error = 'err_userpass'
        if login_error:
            write_data(self, 'login.html', {
                'login_error':login_error,
                })
        self.set_secure_cookie('user',username,settings.cookie_timeout)
        self.redirect(self.get_argument('next','/'))

    def get(self):
        if self.get_current_user():
            self.redirect('/')
            return
        write_data(self, 'login.html', {
            'login_error':None,
            })

class LogoutHandler(BaseHandler):

    def get(self):
        if self.get_current_user() is None:
            self.redirect('/login')
            return
        self.clear_cookie('user')
        self.redirect('/login')
        return

class MonitorHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        write_data(self, 'monitor/monitor.html',{
            })

class ServerHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        write_data(self, 'server/server.html',{
            })

class ManageHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        write_data(self, 'manage/manage.html',{
            })

class AdminHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        write_data(self, 'user/admin.html',{
            })

class TsaltWuApp(tornado.web.Application):

    def __init__(self,settings,**kwargs):
        handlers = [
                (r'/', IndexHandler),
                (r'/login', LoginHandler),
                (r'/logout', LogoutHandler),
                (r'/main', MainHandler),
                (r'/left', LeftHandler),
                (r'/monitor', MonitorHandler),
                (r'/server', ServerHandler),
                (r'/manage', ManageHandler),
                (r'/admin', AdminHandler),
                ]

        go_settings = {}
        go_settings['debug'] = settings.DEBUG
        go_settings['xheaders'] = settings.xheaders
        go_settings['xsrf_cookies'] = settings.xsrf_cookies
        go_settings['template_path'] = settings.template_path
        go_settings['static_path'] = settings.static_path
        go_settings['cookie_secret'] = settings.cookie_secret
        go_settings['login_url'] = '/login'
        tornado.web.Application.__init__(self, handlers, **go_settings)




urls = [
        ]


def run(options):
    server = tornado.httpserver.HTTPServer(TsaltWuApp(settings))
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    from tornado.options import define, options
    define('processes', default=1, help='process number. 0 is max processes', type=int)
    #define('host', default=settings.HOST, help='run on the given ip', type=str)
    define('port', default=8088, help='run on the given port', type=int)
    define('daemonize', default=False, help='whether to detach from terminal', type=bool)
    define('workdir', default='.', help='change to this directory when daemonizing', type=str)
    tornado.options.parse_command_line()
    run(options)
