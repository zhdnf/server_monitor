from faker import Faker
import mysql
import time
import random

def mysql_datas_maker():
    array = []
    for i in range(1,101):
        time_l = int(time.time())
        cpu_percent = random.randint(1,100)
        array.append((cpu_percent, time_l))
    
    return array

if __name__ == '__main__':
    ms = mysql.Mysql()
    
    sql = "insert into sysinfo(cpu_percent, time) values (%s,%s)"
    
    arrays = mysql_datas_maker()
    
    for array in arrays:
        ms.insert(sql,  array)

