import mysql
import time 
import random 

sql_1 = 'insert into sysinfo values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

local_time = 1549850438

mysql = mysql.Mysql()

for i in range(0,1500):
    cpu = random.randint(0,100)
    array = (1, cpu, 0, 0, 0, 0, 0, 0, 0, local_time)
    mysql.insert(sql_1, array)
    local_time = local_time + 2
   

