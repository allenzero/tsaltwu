#!/usr/bin/env python

import tornado.options
from tornado.options import define, options
from main import run

define('processes', default=1, help='process number. 0 is max processes', type=int)
#define('host', default=settings.HOST, help='run on the given ip', type=str)
define('port', default=8088, help='run on the given port', type=int)
define('daemonize', default=False, help='whether to detach from terminal', type=bool)
define('workdir', default='.', help='change to this directory when daemonizing', type=str)

def startup():

    tornado.options.parse_command_line()
    print 'port: %s' % (options.port)
    if options.daemonize:
        from daemonize import become_daemon
        become_daemon(our_home_dir=options.workdir)
    run(options)


if __name__ == '__main__':

    startup()


