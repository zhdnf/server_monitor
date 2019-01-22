# mysql config
MYSQL_CONFIG = {
    'host' : '127.0.0.1',
    'port' : 3306,
    'user' : 'root',
    'passwd' : '123',
    'database' : 'server_monitor',
    'charset' : 'utf8mb4',
}

# tornado config
TORNADO_CONFIG = {
    "static_path" : "/root/server_monitor/app/static",
    "template_path": "/root/server_monitor/app/templates",
}

# gprc_server
GPRC_IP = '192.168.203.155'
GPRC_PORT = '50051'
