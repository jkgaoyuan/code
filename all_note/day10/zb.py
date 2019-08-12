##########僵尸进程
import os
import time
print('starting')
retval = os.fork()
if retval:
    print('f process')
    time.sleep(30)
    print('f process wearkup')
else:
    print('s process')
    time.sleep(10)
    print('s process wearkup')
    exit()