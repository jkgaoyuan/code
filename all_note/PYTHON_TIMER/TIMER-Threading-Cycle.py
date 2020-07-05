#timer1 无限循环
import threading  ##导入线程模块
def sayhello():
        print('hello')
        global t
        ##使用全局变量,
        t = threading.Timer(2.0, sayhello)
        t.start()
t = threading.Timer(2.0, sayhello)
t.start()
