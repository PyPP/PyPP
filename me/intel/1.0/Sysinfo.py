import cpuinfo
import psutil
import GPUtil
import platform
from plyer import notification
import socket
import requests
from datetime import datetime
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)

class GPUInfo:
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        GPUName = gpu.name
        GPUMemory = f"{gpu.memoryTotal}MB"
        list_gpus.append((
            GPUName, GPUMemory
        ))
class DSKInfo:
    partition = psutil.disk_partitions()
    partition_usage = psutil.disk_usage('/')
    DiskUsage = f'{get_size(partition_usage.used)}'
    DiskSpaceFree = f'{get_size(partition_usage.free)}'
    DiskSpace = f'{get_size(partition_usage.total)}'

class CPUInfo:
    CPUName = cpuinfo.get_cpu_info()['brand_raw']

class RAMInfo:
    svmem = psutil.virtual_memory()
    TotalRAM = f'{get_size(svmem.total)}'
    AvailableRAM = f'{get_size(svmem.available)}'

class SystemInfo:
    system = platform.uname()
    SystemType = f'{system.machine}'
    SystemVersionShort = f'{system.release}'
    SystemVersionFull = f'{system.version}'
    SystemOS = f'{system.system}'
class GetWifiInfo(object):
    Hostname = socket.gethostname()
    IP = socket.gethostbyname(Hostname)
    url = "https://www.google.com/"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        IsConnected = True
    except (requests.ConnectionError, requests.Timeout) as exception:
        IsConnected = False

class GetTimeInfo(object):
    now = datetime.now()
    FullTime = now.strftime("%H:%M:%S")
    ShortTime = now.strftime("%H:%M")
    Short12Hr = now.strftime('%I:%M')
    Full12Hr = now.strftime('%I:%M:%S')
    Year = now.strftime('%Y')
    Month = now.strftime('%m')
    Day = now.strftime('%d')
    Date = Day + '-' + Month + '-' + Year