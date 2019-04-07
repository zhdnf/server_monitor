import tornado.web
from app.handlers.common import BaseHandler


class MainHandler(BaseHandler):
    '''
    @tornado.web.authenticated
    def get(self):
        self.write(self.render("index.html", user=self.get_current_user()))
        # static_path=self.settings['static_path']))
    '''
    def get(self):
        self.write(self.render('index.html'))

class Page404Handler(BaseHandler):
    def get(self):
        self.write(self.render("web/404.html"))


