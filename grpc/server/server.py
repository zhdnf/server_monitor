import psutil
from concurrent import futures
import grpc 
import time
import systeminfo_pb2, systeminfo_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Probe(systeminfo_pb2_grpc.SysinfoServicer):
    def GetSysInfo(self, request, context):
        print(request.cpu)
        return systeminfo_pb2.Response(action="OK")
        '''
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory()[2]
        swap = psutil.swap_memory()[3]
        disk_counters = psutil.disk_io_counters()
        net_counters = psutil.net_io_counters()
        return systeminfo_pb2.Response(cpu=cpu, mem=mem, swap=swap, disk_r=disk_counters[2],
                                    disk_w = disk_counters[3], net_s=net_counters[0],
                                    net_r = net_counters[1])
        '''
    def GetProcesses(self, request_iterator, context):
        '''
        pss = psutil.process_iter()
        for ps in pss:  
            yield systeminfo_pb2.Process(pid=ps.pid, name=ps.name(), cpu=ps.cpu_percent(),
                                      mem=ps.memory_percent())
        ''' 
        print(request_iterator)
        for i in request_iterator:
            print(i)
        return systeminfo_pb2.Response(action="OK")

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    systeminfo_pb2_grpc.add_SysinfoServicer_to_server(Probe(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:   
        server.stop(0)


if __name__  == '__main__':
    server()
