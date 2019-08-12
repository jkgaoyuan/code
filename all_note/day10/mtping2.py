###使用class 方法
import subprocess
import threading
class MyClass:
    def __init__(self, a):
        self.a = a

    def __call__(self):
        result = subprocess.run(
            'ping -c2 %s &> /dev/null' % self.a,
            shell=True
        )
        if result.returncode == 0:
            print('%s:up' % self.a)
        else:
            print('%s:down' % self.a)

if __name__ == '__main__':
    ips = ['176.233.6.%s' % i for i in range(1, 255)]
    for ip in ips:
        t = threading.Thread(target=MyClass(ip))
        t.start()


