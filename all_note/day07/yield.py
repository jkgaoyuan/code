ips = ('192.168.1.%s' % i for i in range(1,255))
for i in ips:
    print(i)

def mygen():
    yield 100
    n = 10 + 20   ####yield 多次返回中间值
    yield n
    yield 'hello world'
mg =mygen()  ###生成器
for i in mg:
    print(i)
