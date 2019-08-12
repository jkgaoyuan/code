########僵尸进程 又父进程解决僵尸进程
###watch -n1 ps a  用这个 命令在终端查看进程是否为僵尸进程
import os
import time

print('starting...')
retval = os.fork()
if retval:
    print('父进程')
    time.sleep(20)
    print('父进程，继续')
    result = os.waitpid(-1, 1)  # 不挂起父进程，处理子进程
    print(result)  # 子进程是僵尸进程，返回(子进程PID, 0)
    time.sleep(10)
    print('父进程，结束')
else:
    print('子进程')
    time.sleep(10)
    print('子进程，结束')