## 默认 产生8 位的 密码, 可以输入数字产生自定义长度密码
import random
def genpass(n = 8):
    alist = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    passwd = ''
    for i in range(int(n)):
        blist = random.choice(alist)
        passwd += blist

    print(passwd)

print('输入密码长度,若不输入则默认产生8位密码')
n = input('passwd_length:')
if n == '':
    n = 8
genpass(n)


###错误写法
# def genpass(len=8):
#     import random
#     alist = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
#     for i in range(len):
#         blist = random.choice(alist)
#     return blist
#
# passwd = ''
# a = int(input('passwd_length:'))
# genpass(a)
# passwd += blist
# print(passwd)


##产生定长的斐波那契数列
# def gen_fib():
#     alist = [0,1]
#     s1 = 0
#     num = intrange(input('num:'))
#     for i in num:
#         alist.append(alist[-1] + alist[-2])
#
#     print(alist)
# gen_fib()
