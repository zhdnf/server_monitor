import sys
sys.path.append("/root/server_monitor")
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from config import TORNADO_CONFIG
import tornado.ioloop
import tornado.web
import random
import json
import time

class Application(tornado.web.Application):
    def __init__(self):
        self.handlers = [
                            (r"/", MainHandler),
                            (r"/cpu", CpuPercentHandler),
                            (r"/swap", SwapHandler),
                            (r"/mem", MemHandler),
                            (r"/disk", DiskHandler),
                            (r"/disk_io", Disk_ioHandler),
                            (r"/net_io", Net_ioHandler),
                            (r"/process", ProcessHandler),
                            (r"/proc", ProcHandler)
                        ]
        self.settings = TORNADO_CONFIG

        super(Application,self).__init__(self.handlers, **self.settings)

class BaseHandler(tornado.web.RequestHandler):
    def render(self, template_name, **kwargs):
        template_dirs = []
        if self.settings.get('template_path', ''):
            template_dirs.append(self.settings['template_path'])
        env = Environment(loader = FileSystemLoader(template_dirs))

        try:
            template = env.get_template(template_name)
        except TemplateNotFound:
            raise TemplateNotFound(template_name)
        
        content = template.render(kwargs)
        
        return content

class MainHandler(BaseHandler):

    def get(self):
        self.write(self.render("index.html"))
        # static_path=self.settings['static_path']))

class CpuPercentHandler(BaseHandler):
    def get(self):
        self.write(self.render("cpu.html"))
    
    def post(self):
        ret = {'times' : "01:02", 'num': str(random.randint(0,100))}  

        self.write(json.dumps(ret))

class SwapHandler(BaseHandler):
    def get(self):
        self.write(self.render("swap.html"))

    def post(self):
        num = random.randint(1,100)
        
        self.write(str(num))

class MemHandler(BaseHandler):
    def get(self):
        self.write(self.render("mem.html"))

    def post(self):
        num = random.randint(1,100)
        
        self.write(str(num))

class DiskHandler(BaseHandler):
    def get(self):
        self.write(self.render("disk.html"))

    def post(self):
        ret = {'times' : "20:02", 'num': str(random.randint(0,100))}  
        self.write(json.dumps(ret))

class Disk_ioHandler(BaseHandler):
    def get(self):
        self.write(self.render("disk_io.html"))

    def post(self):
        ret = {'times' : "01:00", 'num': str(random.randint(0,100))}  

        self.write(json.dumps(ret))


class Net_ioHandler(BaseHandler):
    def get(self):
        self.write(self.render("net_io.html"))
    
    def post(self):
        ret = {'times' : "01:02", 'num': str(random.randint(0,100))}  

        self.write(json.dumps(ret))

class ProcessHandler(BaseHandler):
    def get(self):
        self.write(self.render("process.html"))

    def post(self):
        res = []
        for i in range(0,5):
            dit={}
            dit = {'names':'pid\n\nname', 'cpu':random.randint(1,10),'mem':random.randint(1,10)}
            res.append(dit)

        self.write(json.dumps(res))


class ProcHandler(BaseHandler):
    def get(self):
        self.write(self.render("proc.html"))

    def post(self):
        res = []
        for i in range(0,5):
            dit={}
            dit = {'names':'pid\n\nname', 'cpu':random.randint(1,10),'mem':random.randint(1,10)}
            res.append(dit)

        self.write(json.dumps(res))

if __name__ == "__main__":
    application = Application()

    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
