import sys
sys.path.append("/root/server_monitor")

import psutil
import time
from concurrent import futures
import grpc 

from conf.config import GRPC_PORT
from db import mysql

import systeminfo_pb2, systeminfo_pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Probe(systeminfo_pb2_grpc.SysinfoServicer):
    def GetSysInfo(self, request, context):

        # print(request.cpu, request.vmem,request.smem, request.disk, request.disk_i, request.disk_o,request.net_i, request.net_o)

        time_l = time.time()

        ms = mysql.Mysql()
        query_sql = "select * from user where ip = '%s'"
        query_array = (request.ip)

        res = ms.query(query_sql, query_array)

        insert_sql = "insert into sysinfo values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        insert_array = (res[0]['uid'], request.cpu*10, request.vmem*10,
        request.smem*10, request.disk*10, request.disk_i*10, request.disk_o*10,
        request.net_i*10, request.net_o*10, time_l)

        ms.insert(insert_sql, insert_array)

        ms.close()

        return systeminfo_pb2.Response(action="OK")
    
    def GetProcesses(self, request_iterator, context):
        time_l  = time.time()
        res = []

        for i in request_iterator:
            row = {}
            row['pid'] = i.pid
            row['pname'] = i.name
            row['pcpu'] = i.cpu
            row['pmem'] = i.mem
            ip = i.ip

            res.append(row)

        res.sort(key = lambda x: x["pmem"], reverse=True) 
        
        ms = mysql.Mysql()

        query_sql = "select * from user where ip = '%s'"
        query_array = (ip,)
        res_sql = ms.query(query_sql, query_array)

        insert_sql = "insert into process values(%s, %s, '%s', %s, %s, %s)"

        for i in res[0:5]:
            
            print(i['pcpu'])
            insert_array = (res_sql[0]['uid'], i['pid'], i['pname'],
            i['pcpu']*10, i['pmem']*10, time_l)
            
            ms.insert(insert_sql, insert_array)

        ms.close()

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
