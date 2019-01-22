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
                            (r"/process", ProcessHandler)
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
    def _get_datas(self):
        res  = json.dumps(query_result)
        return res

    def get(self):
        self.write(self.render("cpu.html"))

    def post(self):
        ret = [{'dates':'2012-09-01','values':random.randint(1,200)}]
        print(ret)
        ret = json.dumps(ret)

        self.write(ret)

class SwapHandler(BaseHandler):
    def get(self):
        self.write(self.render("swap.html"))

    def post(self):
        num = random.randint(1,100)
        
        self.write(str(num))

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


if __name__ == "__main__":
    application = Application()

    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
