import sys
sys.path.append("/root/server_monitor")
import tornado.ioloop
import tornado.web
from tornado import httpserver

from application import App


if __name__ == "__main__":

    app = App()
    http_server = httpserver.HTTPServer(app)
    http_server.bind(7777)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()
