from config import MYSQL_CONFIG
import pymysql

# create table cpu template
cpu_sql = " create table cpu( \
            id int not null AUTO_INCREMENT, \
            cpu_percent int not null, \
            time int not null, \
            PRIMARY KEY( id )) "

class Mysql:
    
    def __init__(self):
        self.conn = pymysql.connect(**MYSQL_CONFIG)
        self.cur  = self.conn.cursor()

    def create_database(self, database_name):
        status = self.cur.execute("show database like '%s'"%database_name)
        if status == True:
            pass
        else:
            self.cur.execute("create database %s"%database_name)

    def use_database(self, database_name)
        self.cur.execute("use %s"%databases_name)

    def create_table(self, table_name):
        status = self.cur.execute("show table like '%s'"%table_name)
        if status == True:
            pass
        else:
            self.cur.execute("create table %s"%table_name)

    def query(sql, cond=()):
        if cond == ():
            self.cur.execute(sql)
            res = self.cur.fetchone()
        else:
            self.cur.execute(sql % condition)
            res = self.cur.fetchone()

        result = []
        for r in res:
            row = {}
            for i in range(len(index)):
                row[index[i][0]] = r[i]
            result.append(row)

        return result

    def query_fetchall(sql, cond=()):
        if cond == ():
            self.cur.execute(sql)
            res = self.cur.fetchall()
        else:
            self.cur.execute(sql % condition)
            res = self.cur.fetchall()
        
        result = []
        for r in res:
            row = {}
            for i in range(len(index)):
                row[index[i][0]] = r[i]
            result.append(row)

        return result
        
    def insert(sql, cond=()):
        try:
            if cond == ():
                res = self.cur.execute(sql)
            else:
                res = self.cur.execute(sql % condition)
            self.commit()
        except:
            self.rollback()

    def close():
        self.conn.close()

    def commit():
        self.conn.commit()

    def rollback():
        self.conn.rollback()

def trigger_init(ip)
    mysql = Mysql()
    name = ip + '_monitor'
    mysql.create_database(name)
    mysql.use_database(name)
    mysql.create_table(cpu_sql)
    mysql.close()
    mysql.close()


if __name__ == '__main__':
    
