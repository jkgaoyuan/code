# stack = []
# def inputtext():
#     data = input('data:').strip()
#     if data:
#         stack.append(data)
#     else:
#         print('null ')
#
# def output():
#     if stack:
#         print('stack is %s' % stack)
#     else:
#         print('null')
# def view():
#     print(stack)
# def menu():
#     text = '''
#     0 input
#     1 output
#     2 view
#     3 exit
#     '''
#     while 1:
#         choise = input(text).strip()
#         if choise not in ['0','1','2','3']:
#             print('text erro')
#         elif choise == '0':
#             inputtext()
#         elif choise == '1':
#             output()
#         elif choise == '2':
#             view()
#         elif choise == '3':
#             print('baby')
#             break
#         else:
#             continue
# if __name__ == '__main__':
#     menu()



################ 完成  入栈出栈 和查看
# stack = []
#
# def inputtext():
#     data = input().strip()
#     if data:
#         stack.append(data)
#     else:
#         print('text is null')
# def outout():
#     if stack:
#         print('stack is %s' % stack)
#     else:
#         print('null')
# def view():
#     print(stack)
#
# def menu():
#     cmds = {'0':inputtext,'1':outout,'2':view}   ####cmds 是个字典
#     text = '''
#       0 input
#      1 output
#      2 view
#      3 exit
#     '''
#     while 1:
#         choise = input(text).strip()
#         if choise not in ['0','1','2','3']:
#             print('text erro')
#             continue
#         if choise == '3':
#             print('baby')
#             break
#         cmds[choise]()
#
# if __name__ == '__main__':
#     menu()
#########################


####### subprocess 测试
# import subprocess
# subprocess.run('ls ~', shell= True)
# result = subprocess.run('ls abcd', shell = True)
#
# print(
# result.returncode)
# result =subprocess.run('id root id abca', shell=True,
#                        stdout=subprocess.PIPE,
#                        stderr=subprocess.PIPE
#                        )
# print(
# result.stdout)
# print(
# result.stderr)
#
#
#
# ###bytes > str
#
# print(result.stdout.decode)
# print(result.stderr.decode)
#
# hi = '你好 dc'
# print(hi.encode())
#
# a, b = 10, 20
# print(a)
# print(b)
# a, b = b, a
# print(a)
# print(b)
# e, f = [10, 20]
# print(type(e))
# m, n = (100, 200)
# print(type(m))
# q, w = {'name':'tom','age':'22'}
# print(type(q))
# print(w)
#
# # reversed('abcdefg')
# print(reversed('abcdefg'))
# print(list(reversed('abc')))
#
# for  i in reversed('abcd'):
#     print(i)
#
# print('abcd'[::-1])
# print('abcd'[0:-1])
#
# s1 = 'hello world'
# s2 = 'HAO 123'
# s3 = 'hao123'
# s4 = '7298302'
# s5 = '\thello world\n'
# s1.center(48)
# print(s1.center(48))
# print(s1.center(48, '*'))
# print(s1.ljust(48, '#'))
# print(s1.rjust(48, '#'))
# print(s1.upper())
# print(s2.lower())
# print(s5.strip())
# print(s5.rsplit())


# print(s1.startswith('h'))
# print(s1.startswith('the'))
# print(s1.endswith('ab'))
# print(s1.replace('e', '1'))
# print(s1.replace('ll','ab'))
# print(s1.split())

#
# print(
# 'hello.world.ni.hao'.split('.')
# )
#
# print(
# '-'.join(['abc', 'hello', 'hao']))

# import random

import string
#
# all_chs = string.ascii_letters + string.digits
# all_choisse = random.choices(all_chs)
# print(all_choisse)



# def valeurs_pgcd():  # creer un tuple contenant les deux nombres dont on cherche le pgcd

# import random
# reste = random.choice((2, 3, 5, 9, 10)) * random.choice((7, 11, 13,
#             17, 19, 23, 31))
# diviseur = reste * random.randrange(1, 10)
# for dummy in range(random.randrange(2, 5)):
#         (diviseur, reste) = (diviseur * random.randrange(1, 10) + reste,diviseur)
# # return (diviseur, reste)
#
#
# print(diviseur, reste)
#
# print('%2s is %3s years old' % ('tom', 22))
# print('%s is %s years old' % ('tom', 22))

# info = dict([('name', 'tom'), ('age', 20), ('mail', 'tom@tedu.cn')])
#
# for key in info:
#     print(key,info[key])
#
# print('%(name)s is %(age)s years old' % info)
# print('%s is %s years old' % (info['name'], info['age']))

def gen_fib(n):
    fib = [0,1]
    for i in range(n -2 ):
        fib.append(fib[-1] + fib[-2])

    return fib

# mylist =  [5, 8, 10, 13]
# for i in mylist:
#     print(gen_fib(i))

n = int(input('length:'))
print(gen_fib(n))

# python的项目 持续化集成 cacd