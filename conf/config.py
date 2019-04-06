import os

BASE_DIR = os.getcwd()

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
    "static_path"  :  os.path.join(BASE_DIR, "/app/static"),
    "template_path":  os.path.join(BASE_DIR, "app/templates"),
    "cookie_secret":  "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    # "xsrf_cookies" : True,
    "login_url" : "/login"
}

# gprc_server
GPRC_IP = '192.168.203.155'
GPRC_PORT = '50051'
