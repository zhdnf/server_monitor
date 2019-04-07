from app.handlers.common import BaseHandler
from utils.account import authenticate

class RegisterHandler(BaseHandler):
    def get(self, *args, **kwargs):
        print("register")
        self.render('signup.html')

    def post(self, *args, **kwargs):
        print("register post")
        
        username = self.get_argument('username')
        email = self.get_argument('email')
        password1 = self.get_argument('password1')
        password2 = self.get_argument('password2')

        if username and password1 and (password1 == password2):
            pass
        else:
            self.write({'msg': 'register fail'})


class LoginHandler(BaseHandler):
    def get(self,*args,**kwargs):
        if self.current_user: #若用户已登录
            self.redirect('/') #那么直接跳转到主页
        else:
            nextname = self.get_argument('next') #将原来的路由赋值给nextname
            self.render('login.html', nextname= nextname )#否则去登录界面

    def post(self,*args,**kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')

        passed = authenticate(username,password)

        if passed: 
            self.session.set('user_info',username) #将前面设置的cookie设置为username，保存用户登录信息
            next_url = self.get_argument('next') # 获取之前页面的路由

            if next_url:
                self.redirect(next_url) #跳转主页路由
            else:
                self.redirect('/')
        else:
            self.write({'msg':'login fail'}) #不通过，有问题

class LogoutHandler(BaseHandler):
    def get(self, *args, **kwargs): 
        #self.session.set('user_info','') #将用户的cookie清除
        self.session.delete('user_info')
        self.redirect('/login')
