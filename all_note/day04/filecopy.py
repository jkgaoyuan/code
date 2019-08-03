# import   shutil
# fsrc = open('/etc/passwd', 'rb')
# fdst = open('/tmp/mima', 'wb')
# shutil.copyfileobj(fsrc, fdst)
# fsrc.close()
# fdst.close()
# shutil.copy2('/etc/hosts', '/tmp/zhuji')
# shutil.copy('/etc/hosts', '/tmp/zhuji.txt')
# shutil.copy('/etc/hosts', '/tmp/')
# shutil.copytree('/home/student/nsd1903', '/tmp/anquan')  ###注意空格
# shutil.move('/tmp/anquan', '/var/tmp/anuan')
# shutil.chown('/tmp/mima', user='named',group='named')

##### str 和 bytes 之间的转换  subpress 执行用户创建命令

import subprocess
subprocess.run('ls ~', shell=True)
result = subprocess.run('ls ~/nsd1903', shell=True)
print(result.returncode)
result = subprocess.run('id root; id named', shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

print(result.stdout, result.stderr)

print(result.stdout.decode())  ## byses 转换 str

hi = '你好tom'
print(hi.encode())  ## str 转换 byses

data = hi.encode() ## bytes 转换 str
print(data.decode())


### 链式多重赋值

# a = b = 10
# print(a, b)
#
# b = 20
# print(a, b)
#
# alist = blist = [10, 20, 30]
# blist[-1] = 5
# print(blist, alist)
#
#

