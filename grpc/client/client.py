from __future__ import print_function

import psutil
import time
import grpc

import systeminfo_pb2
import systeminfo_pb2_grpc

def make_ps(pid, name, cpu, mem):
    return systeminfo_pb2.Process(pid=pid, name=name, cpu=cpu, mem=mem)

def generate_ps():
    pss = psutil.process_iter()
    for ps in pss:
        yield make_ps(ps.pid, ps.name(), ps.cpu_percent(), ps.memory_percent())

    
def run():
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
    cpu = psutil.cpu_percent()
    '''
    with grpc.insecure_channel('192.168.203.155:50051') as channel:
        stub = systeminfo_pb2_grpc.SysinfoStub(channel)

        response  = stub.GetSysInfo(systeminfo_pb2.Sysstatus(cpu=cpu))
    '''

    with grpc.insecure_channel('192.168.203.155:50051') as channel:
        stub = systeminfo_pb2_grpc.SysinfoStub(channel)

        response = stub.GetProcesses(generate_ps())

        print(response.action)

if __name__ == '__main__':
    run()
