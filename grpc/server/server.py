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
        print(request.cpu)
        return systeminfo_pb2.Response(action="OK")

    def GetProcesses(self, request_iterator, context):
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
