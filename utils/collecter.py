import psutil
import time

def get_cpu():
    return psutil.cpu_percent(interval=1)

def get_vmem():
    return psutil.virtual_memory().percent

def get_smem():
    return psutil.swap_memory().percent

def get_disk():
    return psutil.disk_usage('/').percent

# KB/s
def get_disk_io():
    i_bytes_1 = psutil.disk_io_counters().write_bytes
    o_bytes_1 = psutil.disk_io_counters().read_bytes
    time.sleep(1)
    i_bytes_2 = psutil.disk_io_counters().write_bytes
    o_bytes_2 = psutil.disk_io_counters().read_bytes
    i = (i_bytes_2 - i_bytes_1) / 1024
    o = (o_bytes_2 - o_bytes_1) / 1024
    return (i, o)

# Kbps
def get_net_io():
    i_bytes_1 = psutil.net_io_counters().bytes_recv
    o_bytes_1 = psutil.net_io_counters().bytes_sent
    time.sleep(1)
    i_bytes_2 = psutil.net_io_counters().bytes_recv
    o_bytes_2 = psutil.net_io_counters().bytes_sent
    i = (i_bytes_2 - i_bytes_1) / 1024  * 8 
    o = (o_bytes_2 - o_bytes_1) / 1024  * 8
    return (i, o)

def get_process():
    return psutil.process_iter()

# def get_temperatures():
    # return psutil.sensors_temperatures()

# def get_battery():
    # return psutil.sensors_battery()

if __name__ == '__main__':
    print('cpu:',get_cpu())
    print('vitual memory:',get_vmem())
    print('swap memory:',get_smem())
    print('disk:',get_disk())
    print('disk read:',get_disk_io()[0])
    print('disk write:',get_disk_io()[1])
    print('network rv:',get_net_io()[0])
    print('network send:',get_net_io()[1])
    print("processes:", get_process())
    # print('temperatures:', get_temperatures())
    # print('battery:', get_battery())

