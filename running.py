#!/usr/bin/python
#
# http://stackoverflow.com/questions/1420426/calculating-cpu-usage-of-a-process-in-linux 
#

from time import sleep
import os
import os.path
import sys

name = sys.argv[0]

# get total cpu time
def get_cpu_jiffies():
    "Get total cpu time at the given time."
    cpu_time = 0
    with open("/proc/stat") as f:
        for line in f:
            if line.startswith("cpu "):
                cpu_jiffies = line.split()[1:]
                cpu_time = sum([int(x) for x in cpu_jiffies])
    return cpu_time

def get_jiffies(proc):
    "Get process's current cpu time used over time"
    stats = os.path.join("/proc", proc, "stat")
    with open(stats) as statfile:
        content = statfile.read()
        content = content.split()
        return int(content[13]) + int(content[14])

def find_process_by_name(name):
    "Searches through /proc to find certain process by name"
    # get all directories from /proc which name is a number 
    # (get all process dirs)
    procs = [x for x in os.listdir('/proc') if os.path.isdir("/proc/" + x) 
                and x.isdigit()]

    # go through all processes and find plugin containers
    for proc in procs:
        path = os.path.join("/proc", proc, "status")
        with open(path) as fd:
            pname = fd.readlines()[0]
            pname = pname.split()[1]
            if proc.startswith(name):
                return proc

pid = find_process_by_name("plugin-conta")
last_prc = get_jiffies(pid)
last_cpu = get_cpu_jiffies()
while 1:
    sleep(1)
    new_prc = get_jiffies(pid)
    new_cpu = get_cpu_jiffies()
    time = 100 * (new_prc - last_prc) / (new_cpu - last_cpu)
    print(time)
    last_prc = new_prc
    last_cpu = new_cpu
