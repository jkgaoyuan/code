import  os
print('Starting')
retval = os.fork()       ###调用自进程 后剩余的代码会在父进程先(注意父进程)执行一次,子进程在执行一次, 所以会显示两个 hello world
if retval:
    print('hello from parent')
else:
    print('hello from child')
print('hello from both')