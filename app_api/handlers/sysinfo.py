import sys
sys.path.append('/root/server_monitor')
import json

from app_api.handlers.common import QueryHandler
from db import mysql


class SysInfoHandler(QueryHandler):
        
    def get(self):
        array = self._get_timearray()

        ms = mysql.Mysql()
        res = ms.query_time("sysinfo", array=array)
        res = json.dumps(res)
        self.write(res)


class ProcessHandler(QueryHandler):

    def get(self):
        array = self._get_timearray()

        ms = mysql.Mysql()
        res = ms.query_time("process", array=array)
        res = json.dumps(res)
        self.write(res)


