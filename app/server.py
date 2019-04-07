import sys
sys.path.append("/root/server_monitor")
import tornado.ioloop
import tornado.web
from tornado import httpserver

from application import App

# 延迟时间，秒为单位
delay = 30

# 查询间隔
interval = 60


if __name__ == "__main__":

    app = App()
    http_server = httpserver.HTTPServer(app)
    http_server.bind(7777)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()
