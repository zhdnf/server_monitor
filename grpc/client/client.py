from __future__ import print_function

import psutil
import time
import grpc

import systeminfo_pb2
import systeminfo_pb2_grpc

ip = '192.168.203.166'
grpc_ip = '192.168.203.155'
grpc_port = '50051'
grpc_channel = grpc_ip + ':' + grpc_port

def ps_object(pid, name, cpu, mem):
    return systeminfo_pb2.Process(pid=pid, name=name, cpu=cpu, mem=mem)

def ps_generator():
    pss = psutil.process_iter()
    
    for ps in pss:
        yield ps_object(ps.pid, ps.name(), ps.cpu_percent(), ps.memory_percent())

def sysinfo_object():
    cpu = psutil.cpu_percent()
    return systeminfo_pb2.SysInfo(cpu=cpu)
   
def run():
    
    with grpc.insecure_channel(grpc_channel) as channel:
        stub = systeminfo_pb2_grpc.SysinfoStub(channel)

        response1  = stub.GetSysInfo(sysinfo_object())
        response2  = stub.GetProcesses(ps_generator())

        print(response1, response2)

if __name__ == '__main__':
    run()
