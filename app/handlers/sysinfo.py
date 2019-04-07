import random

from app.handlers.common import BaseHandler

# 延迟时间，秒为单位
delay = 30

# 查询间隔
interval = 60

class CpuPercentHandler(BaseHandler):
    def get(self):
        self.write(self.render("cpu.html"))
    
    def post(self):
        global delay
        global local_time

        local_time = time.time() 
        query_time = local_time - delay

        res = requests.get('http://192.168.203.155:8888/sys?time1=%d&time2=%d'%(query_time - interval, query_time))
        res = json.loads(res.text)
        
        cpu = res[-1]['cpu']

        time_object = time.localtime(res[-1]['time'])
        time_str = '%d:%d:%d'%(time_object.tm_hour, time_object.tm_min, time_object.tm_sec)

        ret = {'times' : time_str, 'num': str(cpu)}  

        self.write(json.dumps(ret))


class SwapHandler(BaseHandler):
    def get(self):
        self.write(self.render("swap.html"))

    def post(self):
        num = random.randint(1,100)
        
        self.write(str(num))


class MemHandler(BaseHandler):
    def get(self):
        self.write(self.render("mem.html"))

    def post(self):
        num = random.randint(1,100)
        
        self.write(str(num))

class DiskHandler(BaseHandler):
    def get(self):
        self.write(self.render("disk.html"))

    def post(self):
        ret = {'times' : "20:02", 'num': str(random.randint(0,100))}
        self.write(json.dumps(ret))


class DiskIOHandler(BaseHandler):
    def get(self):
        self.write(self.render("disk_io.html"))

    def post(self):
        ret = {'times' : "01:00", 'num':
        str(random.randint(0,100))}

        self.write(json.dumps(ret))


class NetIOHandler(BaseHandler):
    def get(self):
        self.write(self.render("net_io.html"))

    def post(self):
        ret = {'times' : "01:02", 'num':
        str(random.randint(0,100))}

        self.write(json.dumps(ret))


class ProcessHandler(BaseHandler):
    def get(self):
        self.write(self.render("process.html"))
 
    def post(self):
        global delay
        global local_time
 
        local_time = time.time()
        query_time = local_time - delay
 
        datas = requests.get('http://192.168.203.155:8888/process?time1=%d&time2=%d'%(query_time
- interval, query_time))
        datas = json.loads(datas.text)
 
        datas = datas[-5:]
 
        res = []
        for i in range(0,5):
            pid = datas[i]['pid']
            name = datas[i]['pname']
            cpu = datas[i]['pcpu']
            mem = datas[i]['pmem']
            times = datas[i]['time']
 
            dit={}
            dit = {'names':'%d\n\n%s'%(pid, name), 'cpu': cpu, 'mem':mem}
            res.append(dit)
 
        self.write(json.dumps(res))

class ProcHandler(BaseHandler):
    def get(self):
        self.write(self.render("proc.html"))

    def post(self):
        global delay
        global local_time

        local_time = time.time()
        query_time = local_time - delay

        datas = requests.get('http://192.168.203.155:8888/process?time1=%d&time2=%d'%(query_time - interval, query_time))
        datas = json.loads(res.text)

        datas = datas[-5:]

        res = []
        for i in range(0,5):
            pid = datas[i]['pid']
            name = datas[i]['pname']
            cpu = datas[i]['pcpu']
            mem = datas[i]['pmem']
            times = datas[i]['time']

            dit={}
            dit = {'names':'%d\n\n%s'%(pid, name), 'cpu': cpu, 'mem':mem}
            res.append(dit)

        self.write(json.dumps(res))
