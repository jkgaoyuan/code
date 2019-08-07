try:
    n = int(input('number:'))
    result = 100 / n
    print(result)
except ValueError:
    print('interrupe erro')
except ZeroDivisionError:
    print('interrupter erro')
except EOFError:
    print('\nBaby')
    exit()  ##程序遇到exit会彻底结束 不在执行
except KeyboardInterrupt:
    print('baby')
    exit()
print('Done')