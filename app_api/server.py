import sys
sys.path.append("/root/server_monitor/")
import tornado.ioloop
from tornado import httpserver

from application import App


if __name__ == "__main__":
    app = App()
    http_server = httpserver.HTTPServer(app)
    http_server.bind(8888)
    http_server.start()
    tornado.ioloop.IOLoop.current().start()
