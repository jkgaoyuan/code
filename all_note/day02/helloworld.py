# a = [1,2,3,4,5,'a','b','c','d','e']
# print( a[2] + a[5] )
# a = [4,5,6]
# b = a
# a[2] = 3
# print(a[2])


####
# a = {'1':1,'2':[2,4]}
# b = a.copy()  ###浅拷贝(引用):父对象,深拷贝父对象(一级目录),不会随着a的变化而改变,子对象(二级目录)是浅拷贝会随着a的改变而改变
# a['1'] = 3    ### 在a['2'][0] 被修改后对应的变化出现在b['2'][0]上
# sun1 = a['1'] + b['1']
# a['2'][0] = 5  #b['2'][0]的值为 5
# sum2 = a['2'][0] + b['2'][0]
# print(sun1,sum2)
# print(b)
# print(a)
# print(b['2'][0])

# num = int(input('num:'))
# n1 = str(input('test:'))
# print(num)
# print(n1)
# if num > 0 :
#     print('yes')
# else:
#     print('no')
#
# if ' ':
#     print('space is true')
#
# if  0.1:
#     print('none zero')
#
# if -0.0:
#     print('0 is false ')
#
# if ():
#     print('元组 is false')
#
# if  {}:
#     print('字典 是为false')
# if []:
#     print('list is false')
#
# if [1,2]:
#     print('list is true')
#
#
# a = 30
# b = 20
# s = a if a <= b else b
# print(s)
# if a <= b :
#     print(a)
# else:
#     print(b)


# import getpass
# user = str(input('username:'))
# userpass = getpass.getpass('pass:')
#
# if user == 'tom'and userpass == '123':
#     print('\033[32;1m%s access\033[0m' % user)
# else:
#     print('\033[31;1m%s noauth\033[0m' % user)

#使用int型比较str 类型会出错
# scoure = int(input('你的成绩:'))
# if  60 < scoure <= 70:
#     print('及格')
# elif 70 < scoure <= 80:
#     print('可以')
# elif 80 < scoure < 90:
#     print('good')
# elif scoure >= 90:
#     print('nb')
# else:
#     print('fail')
#


#import random
#
# all_list = ['石头','拳头','布']
# computer = random.choice(all_list)
# play = input('你的选择/石头/拳头/布:')
# print('play: %s,computer: %s' % (play,computer) )
#
# if play == '拳头':
#     if computer == '拳头':
#         print('\033[32;1m平局\033[0m')
#     else:
#         print('\033[31;1m失败\033[0m')
#
#
# elif play == '石头':
#     if computer == '石头':
#         print('\033[32;1m平局\033[0m')
#     elif computer == '拳头':
#         print('\033[31;1m赢了\033[0m')
#     else:
#         print('\033[31;1m赢了\033[0m')
# else:
#     if computer == '石头':
#         print('\033[32;1失败\033[0m')
#     elif computer == '拳头':
#         print('\033[31;1m赢了\033[0m')
#     else:
#         print('\033[31;1m平局\033[0m')




import random
pwin = 0
cwin = 0
while cwin < 2 and pwin < 2 :  #人机 赢了不够2次 继续执行

    all_list = ['石头','拳头','布']
    win_list = [['石头','拳头'],['石头','布'],['拳头','布']] #前面是用户后面是电脑
    prompt = '''0 石头
    1 拳头
    2 布
    请选择'''
    computer = random.choice(all_list)
    ind = int(input(prompt))
    play = all_list[ind]
    print('play: %s,computer: %s' % (play,computer) )
    if play == computer:

                print('\033[32;1m平局\033[0m')

    elif [play,computer] in win_list:
                print('\033[31;1m赢了\033[0m')
                pwin += 1


    else:
                print('\033[32;1m失败\033[0m')

                cwin += 1

    if cwin < pwin:
        print('人赢了' )
    else:
        print('电脑赢了')
