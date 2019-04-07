import os

BASE_DIR = os.path.dirname(os.getcwd())

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
    # 一般设置
    "debug" : True,
    "autoreload" : True,
    
    # 模板设置
    "template_path":  os.path.join(BASE_DIR, "app/templates"),

    # 静态文件设置
    "static_path"  :  os.path.join(BASE_DIR, "app/static"),

    # 认证安全
    # "cookie_secret":  "1q2w3e4r",
    "login_url" : "/login",
    # "xsrf_cookies" : True,
    # "xsrf_cookies_version" : None,
}

# gprc_server
GPRC_IP = '192.168.203.155'
GPRC_PORT = '50051'
