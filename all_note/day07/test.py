# # def fun1(name='bob', age): ###
# #     pass
# # def fun2(age,name='bob'): ###带有默认参数的必须写在后面
# #     pass
#
# def fun1(name, age):
#     print('%s is %s years old' % (name, age))
#
# fun1('tom', 20)
# fun1(20, 'tom')
# fun1(age=20, name='tom')
# # fun1(20, name='tom')
# fun1('tom', age=20)
#

# ###############################3
# def fun1(*args): ### *表示 将元组作为参数
#     print(args)
# fun1()
#
# fun1('hao')
#
# fun1('hao', 123, 'tom')
#
#
#
# def fun2(**kwargs):  #### **kwargs 表示字典
#     print(kwargs)
#
# fun2()
# try:
#     fun2(10)
# except (TypeError):
#     print('type erro')
#
# fun2(name='tom', age=200)
#
#
#
#
# def fun3(*args, **kwargs):  ###当然也可以混者用
#     print(args)
#     print(kwargs)
#
# fun3()
# fun3(10, 20, 30, name='tom', age=20)
#
# def add(a, b):
#     return  a + b
#
# nunms = [10, 20 ]
#
# try:
#     add(nunms)
# except (TypeError):
#     print('TypeErro')
#
# print(add(*nunms))
#
# mydict = {'a': 100, 'b': 200}
#
# print(add(**mydict))    ##相当于 a + b


#######随机加减法 错误三次输出正确的答案
#####
from random import randint, choice
def exam():
    cmds = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)
    op = choice('+-')
    result = cmds[op](*nums)  ####*号,表示把序列或字典拆开
    prompt = '%s %s %s =' % (nums[0], op, nums[1])
    counter = 0
    while counter < 3:
        try:
            answer = int(input(prompt))
        except:
            print()
            continue
        if answer == result:
            print('yes')
            break
        print('no')
        counter += 1
    else:
        print('%s %s' % (prompt, result))

def main():
    while True:
        exam()
        try:
            yn = input('continue y/n:').strip()[0]
        except IndexError:
            yn = 'y'
        except (KeyboardInterrupt, EOFError):
            yn = 'n'

        if yn  in 'nN':
            print('baby')
            break
if __name__ == '__main__':
    main()



#
# from random import randint, choice
#
# def exam():
#     cmds = {'+': lambda x, y : x + y, '-':lambda x, y: x - y}
#     nums = [randint(1,100) for i in range(2)]
#     nums.sort(reverse=True)
#     op =  choice('+-')
#     result = cmds[op](*nums)
#     print('%s %s %s' %(nums[0], op, nums[-1]))
#     counter = 0
#     while counter < 3:
#         answer = int(input('you answer:'))
#         if answer == result:
#             print('yes')
#         print('no')
#         counter +=1
#     else:
#         print('%s' % answer)
# def main():
#     while True:
#         exam()
#         yn = input('yes/no').strip()[0]
#         if yn in 'nN':
#             print('baby')
#             break
# if __name__ == '__main__':
#     main()
#
