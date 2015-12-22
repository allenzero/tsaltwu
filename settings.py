#-*- coding: utf-8 -*-
import sys, os, os.path

DEBUG = True
xheaders = True
xsrf_cookies = True
template_path = os.path.join(os.path.dirname(__file__), "templates")
static_path = os.path.join(os.path.dirname(__file__), "static")
cookie_secret = "wUPzfy3YSQu2zBNOXz2ncH0NDnWVbElalkuJNo8PWNc="
cookie_timeout = 1 #天
BASE_URL = 'http://192.168.1.114:8088'

MONGO_ACCOUNT = ('10.10.1.38',27087)
MYSQL_ACCOUNT = ('root', '123456', '192.168.1.99', '3306', 'tsaltwu')
REIDS_ACCOUNT = ('10.144.132.186', 6379, '123456', 0)

if __name__ == '__main__':
    print templates
