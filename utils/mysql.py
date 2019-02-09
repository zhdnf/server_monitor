import sys
sys.path.append('/root/server_monitor/')
from config import MYSQL_CONFIG
import pymysql

def json_output(index, res):
    result = []
    for r in res:
        row = {}
        for i in range(len(index)):
            row[index[i][0]] = r[i]
        result.append(row)
    
    return result
    

class Mysql(object):
    
    def __init__(self):
        self.conn = pymysql.connect(**MYSQL_CONFIG)
        self.cur  = self.conn.cursor()

    def query(self, sql, cond=()):

        if cond == ():
            self.cur.execute(sql)
            index = self.cur.description
            res = self.cur.fetchone()
        else:
            self.cur.execute(sql % cond)
            index = self.cur.description
            res = self.cur.fetchone()

        return json_output(index, res)
    
    def query_time(self, table_name, array=()):
        
        lens = len(array)

        join_str = ''

        if lens == 0:
            cond = (table_name,)
        elif lens == 1:
            join_str = 'where time = %d'
            cond = (table_name, array[0])
        elif lens == 2:
            join_str = 'where time between %d and %d'
            cond  = (table_name, array[0], array[1])
        else:
            exit(0)

        sql = 'select * from %s ' + join_str
        print(sql%cond) 
        self.cur.execute(sql % cond)
        index = self.cur.description
        res = self.cur.fetchall()
        
        return json_output(index, res)

    def query_fetchall(self, sql, cond=()):

        if cond == ():
            self.cur.execute(sql)
            index = self.cur.description
            res = self.cur.fetchall()
        else:
            self.cur.execute(sql % cond)
            index = self.cur.description
            res = self.cur.fetchall()
        
        return json_output(index, res)
        
    def insert(self, sql, cond=()):

    #try:
        if cond == ():
            res = self.cur.execute(sql)
        else:
            res = self.cur.execute(sql % cond)

        self.commit()
        print("insert sucessful")
    #except:
        #self.rollback()
        #print("insert fail")

    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()
