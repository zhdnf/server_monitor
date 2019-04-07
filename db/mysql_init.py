import pymysql

from conf.config import MYSQL_CONFIG


conn = pymysql.connect(**MYSQL_CONFIG)
cur  = conn.cursor()

# user table
user_sql= " create table user( \
            id int not null AUTO_INCREMENT, \
            name varchar(32) not null, \
            email varchar(32) not null, \
            passwd char(32) not null, \
            last_login datetime not null, \
            PRIMARY KEY( id )) "

# cpu table
sysinfo_sql = " create table sysinfo( \
                uid int not null, \
                cpu int not null, \
                vmem int not null, \
                smem int not null, \
                disk int not null, \
                disk_i int not null, \
                disk_o int not null, \
                net_i int not null, \
                net_o int not null, \
                time int not null ) "

# process table
process_sql = " create table process( \
                uid int not null, \
                pid int not null, \
                pname varchar(20) not null, \
                pcpu int not null, \
                pmem int not null, \
                time int not null )"

# notification table
notification_sql = " create tables notify( \
                     id int not null, \ 
                     message text not null, \
                     date datatime not null,)"

cur.execute('drop database if exists server_monitor')
cur.execute('create database server_monitor')
cur.execute('use server_monitor')
cur.execute(user_sql)
cur.execute(sysinfo_sql)
cur.execute(process_sql)




