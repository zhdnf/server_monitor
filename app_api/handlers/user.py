import sys
sys.path.append('/root/server_monitor')
import json


from app_api.handlers.common import UserOptHandler
from db import mysql

class UserHandler(UserOptHandler):
    
    def _opt_user(self):
        opt = self._get_controller()
        if opt  == 'insert':
            sql = "insert into user values(%d, '%s', '%s', '%s')"
            array = self._get_userinfo()
            print(array)
            mysql.Mysql().insert(sql, cond=array)
        elif opt is ():
            pass
        else:
            print('error')
            
    def get(self):
        if self._get_controller() is not ():
            self._opt_user()

        elif self._get_uid() !=  ((),):
            array = self._get_uid()
            print(array)
            ms = mysql.Mysql()
            sql = "select * from user where email = '123@qq.com'"
            res = ms.query(sql)
            res = json.dumps(res)
            self._opt_user()
            self.write(res)

        else:
            sql = "select max(id) from user"
            res = mysql.Mysql().query(sql)
            res = json.dumps(res)
            self.write(res)


