try:    ###有可能发送异常的语句
    n = int(input('number:'))
    result = 100 / n
except (ValueError, ZeroDivisionError): ##异常1
    print('interrupe erro')

except (EOFError, KeyboardInterrupt): ###异常2
    print('\nBaby')
    exit()
else:   ###else 后面的代码是程序不出错所执行的
    print(result)
finally:  ### 不管是否发生异常都执行的代码
    print('Done')
print('function is end')