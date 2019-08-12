###启动三个线程 先睡三秒在输出 hello
###需要在终端中执行 才可以在 终端中查看到 
import time
import threading
def hello():
    time.sleep(3)
    print('hello')
if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=hello)
        t.start()