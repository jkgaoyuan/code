## 默认 产生8 位的 密码, 可以输入数字产生自定义长度密码
# import random
# def genpass(n = 8):
#     alist = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
#     passwd = ''
#     for i in range(int(n)):
#         blist = random.choice(alist)
#         passwd += blist
#
#     print(passwd)
#
# print('输入密码长度,若不输入则默认产生8位密码')
# n = input('passwd_length:')
# if n == '':
#     n = 8
# genpass(n)


##改进写法
##只导入需要的模块

from random import choice
from string import ascii_letters,digits
all_chs = ascii_letters + digits         ###数字 digits  大写字母+小写字母 ascii_letters
def rendpass(n=8):
    result = ''
    for i in range(n):
        ch = choice(all_chs)
        result += ch
    return result
if __name__ == '__main__':
    print(rendpass())
    # print(rendpass(4))



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
