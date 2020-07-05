##倒计时
import threading
def countdown():
    print('这是延迟调用的方式实现定时计划')
timer = threading.Timer(5,countdown)
##延时时间为 5S
timer.start()

