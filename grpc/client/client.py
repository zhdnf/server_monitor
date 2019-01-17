from __future__ import print_function

import psutil
import time
import grpc
import collecter
import systeminfo_pb2
import systeminfo_pb2_grpc

ip = '192.168.203.166'
grpc_ip = '192.168.203.155'
grpc_port = '50051'
grpc_channel = grpc_ip + ':' + grpc_port


def ps_object(ip, pid, name, cpu, mem):

    return systeminfo_pb2.Process(ip=ip, pid=pid, name=name, cpu=cpu, mem=mem)

def ps_generator():
    pss = collecter.get_process()

    for ps in pss:
        yield ps_object(ip, ps.pid, ps.name(), ps.cpu_percent(), ps.memory_percent())

def sysinfo_object():
    cpu = collecter.get_cpu()
    vmem = collecter.get_vmem()
    smem = collecter.get_smem()
    disk = collecter.get_disk()
    disk_i = collecter.get_disk_io()[0]
    disk_o = collecter.get_disk_io()[1]
    net_i = collecter.get_net_io()[0]
    net_o = collecter.get_net_io()[1]

    return systeminfo_pb2.SysInfo(ip=ip, cpu=cpu, vmem=vmem, disk=disk,
    disk_i=disk_i, disk_o=disk_o, net_i=net_i, net_o=net_o)
   
def run():
    
    with grpc.insecure_channel(grpc_channel) as channel:
        stub = systeminfo_pb2_grpc.SysinfoStub(channel)

        response1  = stub.GetSysInfo(sysinfo_object())
        response2  = stub.GetProcesses(ps_generator())

        print(response1, response2)

if __name__ == '__main__':
    run()
