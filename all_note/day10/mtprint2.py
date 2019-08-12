import time
import threading
def hello(a, b):
    time.sleep(3)
    print('hello', a, b)
if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=hello, args=('aaa', 'bbb'))  ###
        t.start()   # 启动工作线程，调用target(*args)  这里的 *args 是会将 args 拆开 成aaa 和 bbb  就是*args 和 **args