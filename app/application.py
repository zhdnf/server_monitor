from tornado.web import Application

from conf.config import TORNADO_CONFIG
from handlers import *

class App(Application):
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


