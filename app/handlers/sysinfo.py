import random

from app.handlers import BaseHandler


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
        pass
