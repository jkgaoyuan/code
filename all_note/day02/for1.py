# astr = 'hao123'
# alist = ['tom','jerry','bob']
# atuple = (10,20,30,45)
# adict = {'name':'tom','age':'22'}
# for s1 in astr:
#     print(s1)
# for s2 in alist:
#     print(s2)
# for s3 in atuple:
#     print(s3)
# for s4 in adict:
#     print(s4,adict[s4])  # adict[s4] 表示adict中名称为s4 的值
# a2 = 0
# for a1 in range(101):
#
#      a2 += a1
#
# print(a2)

import random
count = 0
num1 = random.randint(1,100)
while count < 5:
    pnum = int(input('num:'))
    count += 1
    if pnum < num1:
        print('xiao')
    elif pnum > num1:
        print('dail')
    else:
        print('duil')
        break
else:
   print('%s :' % num1)
