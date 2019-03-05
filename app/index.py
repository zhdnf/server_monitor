import sys
sys.path.append("/root/server_monitor")
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from config import TORNADO_CONFIG
import tornado.ioloop
import tornado.web
import requests
import random
import json
import time
import re

# 延迟时间，秒为单位
delay = 30

# 查询间隔
interval = 60

class Application(tornado.web.Application):
    def __init__(self):
        self.handlers = [
                            (r"/", MainHandler),
                            (r"/login", LoginHandler),
                            (r"/signup", SignUpHandler),
                            (r"/logout", LogoutHandler),
                            (r"/cpu", CpuPercentHandler),
                            (r"/swap", SwapHandler),
                            (r"/mem", MemHandler),
                            (r"/disk", DiskHandler),
                            (r"/disk_io", Disk_ioHandler),
                            (r"/net_io", Net_ioHandler),
                            (r"/process", ProcessHandler),
                            (r"/proc", ProcHandler),
                            (r"/404", Page404Handler)
                        ]
        self.settings = TORNADO_CONFIG

        super(Application,self).__init__(self.handlers, **self.settings)


class BaseHandler(tornado.web.RequestHandler):

    def get_argument(self, name, strip=True):

        return self._get_argument(name, self.request.arguments, strip)

    def _get_argument(self, name, source, strip=True):
        args = self._get_arguments(name, source, strip=strip)
        if not args:
            return ()
        return args[-1]

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

    def get_current_user(self):
        
        return self.get_secure_cookie("username")


class MainHandler(BaseHandler):
    
    @tornado.web.authenticated
    def get(self):
        self.write(self.render("index.html", user=self.get_current_user()))
        # static_path=self.settings['static_path']))


class CpuPercentHandler(BaseHandler):
    def get(self):
        self.write(self.render("cpu.html"))
    
    def post(self):
        global delay
        global local_time

        local_time = time.time() 
        query_time = local_time - delay

        res = requests.get('http://192.168.203.155:8888/sys?time1=%d&time2=%d'%(query_time - interval, query_time))
        res = json.loads(res.text)
        
        cpu = res[-1]['cpu']

        time_object = time.localtime(res[-1]['time'])
        time_str = '%d:%d:%d'%(time_object.tm_hour, time_object.tm_min, time_object.tm_sec)

        ret = {'times' : time_str, 'num': str(cpu)}  

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
        global delay
        global local_time

        local_time = time.time() 
        query_time = local_time - delay

        datas = requests.get('http://192.168.203.155:8888/process?time1=%d&time2=%d'%(query_time - interval, query_time))
        datas = json.loads(datas.text)
            
        datas = datas[-5:]

        res = []
        for i in range(0,5):
            pid = datas[i]['pid']
            name = datas[i]['pname']
            cpu = datas[i]['pcpu']
            mem = datas[i]['pmem']
            times = datas[i]['time']
           
            dit={}
            dit = {'names':'%d\n\n%s'%(pid, name), 'cpu': cpu, 'mem':mem}
            res.append(dit)

        self.write(json.dumps(res))


class ProcHandler(BaseHandler):
    def get(self):
        self.write(self.render("proc.html"))

    def post(self):
        global delay
        global local_time

        local_time = time.time() 
        query_time = local_time - delay

        datas = requests.get('http://192.168.203.155:8888/process?time1=%d&time2=%d'%(query_time - interval, query_time))
        datas = json.loads(res.text)
            
        datas = datas[-5:]

        res = []
        for i in range(0,5):
            pid = datas[i]['pid']
            name = datas[i]['pname']
            cpu = datas[i]['pcpu']
            mem = datas[i]['pmem']
            times = datas[i]['time']
           
            dit={}
            dit = {'names':'%d\n\n%s'%(pid, name), 'cpu': cpu, 'mem':mem}
            res.append(dit)

        self.write(json.dumps(res))

class LoginHandler(BaseHandler):
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        if username == "user" and password=="123":
            self.set_secure_cookie("username", username)
            self.redirect("/")
        else:
            self.write(self.render("login.html"))

    def get(self):
        if self.get_current_user():
            self.redirect("/")
        else:
            self.write(self.render("login.html"))

class SignUpHandler(BaseHandler):
    _RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
    _RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')

    def post(self):
        # 判断post请求数据
        name = self.get_argument('username')
        email = self.get_argument('email')
        passwd = self.get_argument('password')

        print("name:",name)
        print("email",email)
        print("passwd",passwd)
        
        '''
        # c = self.get_argument('c')

        if name is ():
            name = 0
        if email is () or not _RE_EMAIL.match(email):
            email = 0
        if passwd is () or not _RE_SHA1.match(passwd):
            passwd = 1

        # 查询users是否存在
        res_user = requests.get('http://192.168.203.155:8888/user?email=%s'%email)
        is_user = json.loads(res_user.text)
        
        # user的下个id
        res_id = requests.get('http://192.168.203.155:8888/user')
        uid_num = json.loads(res_id.text)
        
        if datas == []:
            raise NameError('register:failed', 'email', 'Email is already in use.')
        
        uid = uid_num[0]['max(id)']
        sha1_passwd = '%s:%s' % (uid, passwd)
        
        insert_url = 'http://192.168.203.155:8888/user?c=insert&uid=%d&name=%s&email=%s&passwd=%s'%(uid, name, email, sha1_passwd)
        '''    
        if name == "user" and passwd == "123":
            print(123)
            # make session cookie:
            self.set_secure_cookie("username", name)
            self.redirect("/")
            
        self.redirect("/")
        
        # r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly=True)
        # user.passwd = '******'
        # r.content_type = 'application/json' 
        # r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
        # self.write(r)

    def get(self):
        self.write(self.render("signup.html"))

class LogoutHandler(BaseHandler):
    def get(self):
        if self.get_argument("logout") == ():
            self.clear_cookie("username")
            self.redirect("/login")
        

class Page404Handler(BaseHandler):
    def get(self):
        self.write(self.render("404.html"))



if __name__ == "__main__":

    application = Application()

    application.listen(7777)
    tornado.ioloop.IOLoop.current().start()
