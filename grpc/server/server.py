import sys
sys.path.append("/root/server_monitor")

import psutil
from concurrent import futures
import grpc 
import time
from config import GPRC_PORT
from utils import mysql

import systeminfo_pb2, systeminfo_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Probe(systeminfo_pb2_grpc.SysinfoServicer):
    def GetSysInfo(self, request, context):

        print(request.cpu*10, request.vmem*10,request.smem*10, request.disk*10, request.disk_i*10, request.disk_o*10,net_i*10, net_o*10)


        time_l = time.time()

        ms = mysql.Mysql()

        query_sql = "select * from user where ip = '%s'"
        query_array = (request.ip,)
        res = ms.query(query_sql, query_array)

        insert_sql = "insert into sysinfo values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        insert_array = (res[0]['uid'], request.cpu*10, request.vmem*10,
        request.smem*10, request.disk*10, request.disk_i*10, request.disk_o*10,
        net_i*10, net_o*10, time_l)

        ms.insert(insert_sql, insert_array)

        ms.close()

        return systeminfo_pb2.Response(action="OK")
    
    def GetProcesses(self, request_iterator, context):
        time_l  = time.time()
        res = []

        for i in request_iterator:
            row = {}
            row['pid'] = i.pid
            row['name'] = i.name
            row['cpu'] = i.cpu
            row['mem'] = i.mem
            ip = i.ip

            res.append(row)

        res.sort(key = lambda x: x["mem"], reverse=True) 
        
        ms = mysql.Mysql()

        query_sql = "select * from user where ip = '%s'"
        query_array = (ip,)
        res_sql = ms.query(query_sql, query_array)

        insert_sql = "insert into sysinfo values(%s, %s, %s, %s, %s, %s)"

        for i in res[0:5]:
            insert_array = (res_sql[0]['uid'], i['pid'], i['pname'],
            i['pcpu'],i['pmem'], time_l)

            ms.insert_array(insert_sql, insert_array)

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
