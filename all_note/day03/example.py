##使用函数打印出 定长的* 且有初始值
# def pstart(n=30):
#     print('*' * n)
# pstart() #默认30
# pstart(50)

def str(a):
    for i in range(len(a)):
        if i != ' ':
            break

    return a[i:]

s1 = '   hello world'
result = str(s1)
print(result)

def num(alist):
    str = ''
    for i in alist:
        if i in '1234567980':
            str += i
    return str
s1 = 'asdfa1313546wadfaf13314'
a = num(s1)
print(a)