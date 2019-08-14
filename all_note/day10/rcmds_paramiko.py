########使用python的paramiko模考来远程 服务器执行 命令, 在没有ansible的时候可以用来替代ansible 
####cmds 是命令包
##这是文件写法
# import paramiko
# import threading
# def ssh_host(host, user='root', passwd=None, port=22, cmds=None):
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect(hostname=host, port=port, username=user,password=passwd)
#     stdin, stdout, stderr, = ssh.exec_command(cmds)
#     out = stdout.read()
#     err = stderr.read()
#     if out:
#         print('[%s] \033[32;1mout\033[0m:\n%s' %(host, out.decode()))
#     if err:
#         print('[%s] \033[31;1merr\033[0m:\n%s' %(host, err.decode()))
#     ssh.close()
#
# if __name__ == '__main__':
#     hostfile = 'hostaddress'
#     password = 'a'
#     cmds = 'id root; id heibanna'
#     with open(hostfile) as fobj:
#         for line in fobj:
#             ip = line.strip()
#             t = threading.Thread(target=ssh_host,args=(ip,), kwargs={'passwd':password,'cmds':cmds})  ###启动多线程执行
#             t.start()

############### 参数写法         主机ip文件   命令参数
#####python3 rcmds_paramiko.py hostaddress 'id root'
###passwd: ###输入密码 getpass模块
import paramiko
import threading
import getpass
import os
import sys

def ssh_host(host, user='root', passwd=None, port=22, cmds=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=port, username=user,password=passwd)
    stdin, stdout, stderr, = ssh.exec_command(cmds)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('[%s] \033[32;1mout\033[0m:\n%s' %(host, out.decode()))
    if err:
        print('[%s] \033[31;1merr\033[0m:\n%s' %(host, err.decode()))
    ssh.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('\033[32;1mUsage: %s ipfile "commands"\033[0m' % sys.argv[0])
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('\033[32;1mNo such file %s\033[0m' % sys.argv[1])
        exit(2)

    hostfile = sys.argv[1]
    password = getpass.getpass()
    cmds = sys.argv[2]
    with open(hostfile) as fobj:
        for line in fobj:
            ip = line.strip()
            t = threading.Thread(target=ssh_host,args=(ip,), kwargs={'passwd':password,'cmds':cmds})  ###启动多线程执行
            t.start()
