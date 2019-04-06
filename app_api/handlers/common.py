from tornado.web import RequestHandler


class QueryHandler(RequestHandler):

    def get_argument(self, name, strip=True):

        return self._get_argument(name, self.request.arguments, strip)


    def _get_argument(self, name, source, strip=True):
        args = self._get_arguments(name, source, strip=strip)
        if not args:
            return ()
        return (int(args[-1]),)
    
    # 按时间查询
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


class UserOptHandler(QueryHandler):

    def _get_argument(self, name, source, strip=True):
        args = self._get_arguments(name, source, strip=strip)
        if not args:
            return ()
        return args[-1]
    
    # email 查询用户
    def _get_uid(self):
        
        email = self.get_argument("email")

        return (email, )
    
    def _get_controller(self):
        
        return self.get_argument('c')

    def _get_userinfo(self):
        uid = self.get_argument('uid')   
        email = self.get_argument("email")
        passwd = self.get_argument("passwd")
        name = self.get_argument("name")

        return (0, name, passwd, email,)



