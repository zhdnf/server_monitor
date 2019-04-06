import re

from app.handlers import BaseHandler



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
 
