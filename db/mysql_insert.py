import mysql
import time 
import random
from faker import Faker

sql_1 = 'insert into sysinfo values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
sql_2 = "insert into process values(%s, %s, '%s', %s, %s, %s)"
sql_3 = "insert into user values('%s', '%s', '%s')"

local_time = 1550106000

def cpu_insert():
    global local_time

    mysql1 = mysql.Mysql()

    for i in range(0,1500):
        cpu = random.randint(0,100)
        array = (1, cpu, 0, 0, 0, 0, 0, 0, 0, local_time)
        mysql1.insert(sql_1, array)
        local_time = local_time + 2

       
def process_insert():
    global local_time

    mysql2 = mysql.Mysql()
    fake = Faker()

    for i in range(1800):

        for j in range(5):
            pid = random.randint(1,1000)
            cpu = random.randint(0,100)
            mem = random.randint(0,100) 
            name = fake.user_name()
            array = (1, pid, name,  cpu, mem, local_time)
            mysql2.insert(sql_2, array)

        local_time = local_time + 2


def user_insert():
    array = ('zhang','123@qq.com','abc')
    mysql.Mysql().insert(sql_3, array)
    array = ('li','134@qq.com','abc')
    mysql.Mysql().insert(sql_3, array)
    array = ('wang','223@qq.com','abc')
    mysql.Mysql().insert(sql_3, array)
            

if __name__ == "__main__":
    # cpu_insert()
    # process_insert()
    user_insert()

