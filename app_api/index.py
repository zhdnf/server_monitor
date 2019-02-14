import sys
sys.path.append("/root/server_monitor/")
import tornado.ioloop
import tornado.web
import json
from utils import mysql

class QueryHandler(tornado.web.RequestHandler):

    def get_argument(self, name, strip=True):

        return self._get_argument(name, self.request.arguments, strip)


    def _get_argument(self, name, source, strip=True):
        args = self._get_arguments(name, source, strip=strip)
        if not args:
            return ()
        return (int(args[-1]),)

    def _get_timearray(self):
        array = ()

        time1 = self.get_argument("time1")
        time2 = self.get_argument("time2")

        if time1 == time2:   
            array = time1
        elif time1 < time2:
            array = time1 + time2
        else:
            array = time2 + time1
        
        return array


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, world")

class SysInfoHandler(QueryHandler):
        
    def get(self):
        array = self._get_timearray()

        ms = mysql.Mysql()
        res = ms.query_time("sysinfo", array=array)
        res = json.dumps(res)

        self.write(res)

class ProcessHandler(QueryHandler):

    def get(self):
        array = self._get_timearray()

        ms = mysql.Mysql()
        res = ms.query_time("process", array=array)
        res = json.dumps(res)

        self.write(res)

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/sys", SysInfoHandler),
        (r"/process", ProcessHandler),
    ])

    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
