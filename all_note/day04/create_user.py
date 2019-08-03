###### 1. 实现创建用户
###### 2. 提示用户输入用户名
###### 3. 生成8 位随机密码
###### 4. 创建用户设置密码
###### 5. 将用户相关信息写入文件


import sys
import subprocess
# import rendpass

#### 模块调用失败

def adduser(username, passworld, fname):
    result = subprocess.run('id %s' % username,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    if result.returncode == 0:
        print('%s exit ' % username)
        return False   ### 函数遇到return就返回,不再向下执行

    ###useradd
    subprocess.run('useradd %s' % username, shell=True)
    subprocess.run('echo %s | passwd --stdin %s' % (passworld, username), shell=True )

    #写入 用户信息到文件
    info = '''' user info:
    username %s
    password %s
    '''% (username, passworld)
    with open(fname, 'a') as fobj:
        fobj.write(info)
if __name__ == '__main__':

    username = sys.argv[1]

    passworld = rendpass.rendpass

    fname = '/tmp/users.txt'

    adduser(username,passworld , fname)

