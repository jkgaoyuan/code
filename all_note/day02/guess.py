#猜数 错误5次显示正确的数,5次以内显示大或者小 ,猜对了跳出循环
# import random
# num = random.randint(1,100)
# c = 0
# while c < 5:
#     pum = int(input('输入数字:'))
#     c += 1
#     if num < pum:
#         print('大了')
#         continue
#     elif num > pum:
#         print('小了')
#         continue
#     else:
#         print('对了')
#         break
#
# else: ##循环的else 当break时不执行,否则执行为了　在猜错5　次之后　输出真确的答案
#     print('答案是 %s'% num)

import random
all_choises = ['石头','剪刀','布']

win_list = [['石头','布'],['石头','剪刀'],['剪刀','布']]
a = 0
b = 0
pt = '''0 石头
1 剪刀
2 布
:
'''
while a < 2 and b < 2:
    cchoises = random.choice(all_choises)
    ind = int(input(pt))
    you_choise = all_choises[ind]

    print('你的选择%s,电脑的选择%s' % (you_choise,cchoises))
    if [you_choise,cchoises] in win_list:
        print('\033[31;1mYou WIN!!!\033[0m')
        a +=1
    elif you_choise == cchoises:
        print('\033[32;1m平局\033[0m')
    else:
        print('\033[31;1mYou WIN!!!\033[0m')
        b +=1