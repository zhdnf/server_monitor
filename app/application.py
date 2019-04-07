from tornado.web import Application

from conf.config import TORNADO_CONFIG
from handlers import web, user, sysinfo

class App(Application):
    def __init__(self):
        self.handlers = [
                            (r"/", web.MainHandler),
                            (r"/login", user.LoginHandler),
                            (r"/sign_up", user.RegisterHandler),
                            (r"/logout", user.LogoutHandler),
                            (r"/cpu", sysinfo.CpuPercentHandler),
                            (r"/swap", sysinfo.SwapHandler),
                            (r"/mem", sysinfo.MemHandler),
                            (r"/disk", sysinfo.DiskHandler),
                            (r"/disk_io", sysinfo.DiskIOHandler),
                            (r"/net_io", sysinfo.NetIOHandler),
                            (r"/process", sysinfo.ProcessHandler),
                            (r"/proc", sysinfo.ProcHandler),
                            (r"/404", web.Page404Handler)
                        ]
        self.settings = TORNADO_CONFIG

        super(App,self).__init__(self.handlers, **self.settings)


