from tornado.web import Application

from handlers import sysinfo, user

class App(Application):
    def __init__(self):

        self.handler = [
            (r"/user", user.UserHandler),
            (r"/sys", sysinfo.SysInfoHandler),
            (r"/process", sysinfo.ProcessHandler),
        ]

        super(App, self).__init__(handlers=self.handler)

