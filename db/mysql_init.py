import pymysql

MYSQL_CONFIG = {
    'host' : '127.0.0.1',
    'port' : 3306,
    'user' : 'root',
    'passwd' : '123',
    'charset' : 'utf8mb4',
}

conn = pymysql.connect(**MYSQL_CONFIG)
cur  = conn.cursor()

# user table
user_sql= " create table user( \
            id int not null AUTO_INCREMENT, \
            name varchar(32) not null, \
            email varchar(32) not null, \
            passwd char(32) not null, \
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

cur.execute('drop database if exists server_monitor')
cur.execute('create database server_monitor')
cur.execute('use server_monitor')
cur.execute(user_sql)
cur.execute(sysinfo_sql)
cur.execute(process_sql)




