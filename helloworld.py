# print('你好我是jkgao')
# count = 0
# while (count<9):
#     print('The count is:', count)
#     count = count + 1
# print('END')
# numbers = [12, 37, 65, 100, 77, 53] #奇数偶数
# even = []
# odd = []
# while len(numbers) > 0 :
#     number = numbers.pop()
#     if(number % 2 == 0) :
#         even.append(number)
#         print('even=', even)
#     else:
#         odd.append(number)
#         print('odd=', odd)
#
# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''# 字符
# s3 = r'Hello, "Bart"'
# s4 = 'i\'m "ok"'
# s5 = r'''Hello,
# Lisa!'''
# print(n,'\n',f,'\n',s1,'\n',s2,'\n',s3,'\n',s4,'\n',s5,)#

#
# a = 'ABC'
# b = a
# a = 'pi'    #赋值 这里的运算和数学的运算是不一样的》！！！！ 这里是吧b指向a指向的字符
#
# print(b)
# print(a)
#
# b1 = 72
# b2 = 85
# r = (b2-b1)/b1*100
# print('小明成绩提升的百分点 %.1f%%' % r)
# print('%.1f%%' % r) #这里 用%%来表示一个%
# #
# names = ['michel','bob','trcey']
# for name in names :      #for循环
#     print(name)
# #
# sum = 0
# for i in[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum = sum + i
# print(sum)
# #
# sum = 0
# for i in range(101):
#     sum = sum + i
# print(sum)
# #
# # f = list(range(100))  #产生整数数列 这里的范围是从零开始的
# # print(f)
# #100以内的奇数求和
# sum = 0
# n = 99
# while n > 0 :
#     sum = sum + n
#     n = n - 2
# print(sum)
# #循环依次对list中的每个名字打印出Hello, xxx!：
# L = ['Bart', 'Lisa', 'Adam']
# for x in L:                #break and continue 用发和c一样
#     print("hello,%s!" % x)  #这里有要替换的字符的话需要占位符
#     # print('hello,%s!' % x)
#     print('Hello,', x, '!')  #这个写法更符合思维
# #
# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0: # 如果n是偶数，执行continue语句
#         continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
#     print(n)        #也就说满足if语句后continue之后的语句是不执行的
#写出一个死循环
# i = 0
# # i = i + 1
# if i < 0:
#     print(i)
# else:
#     print('erro')
#
#使用list和tuple 有序列表 :tumple 不可变 list 可变
#请用索引取出下面list的指定元素： Apple:Python: Lisa
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# B = L[0]
# print(B[0])
# print(L[0][0],L[1][1],L[-1][-1])


#重要的判断语句 当if的条件满足时就会跳过其他的elif 和 else 。
# if的完整结构:        |
# if <条件判断1>:      |
#     <执行1>         |
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>
#############
# age = 20
# if age >= 6:
#     print('teenager')
# elif age >= 18:
#     print('adult')
# else:
#     print('kid')

# 18.10. 27.
# eg
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# #
# # 低于18.5：过轻
# # 18.5-25：正常
# # 25-28：过重
# # 28-32：肥胖
# # 高于32：严重肥胖
# # 用if-elif判断并打印结果：
# H = 1.75
# W = 80.5
# #BMI = W/pow(H,2) #平方的写法
# BMI = W/(H*H)
# BMI
# print('BMI=%.1f' % BMI)
# if BMI<=18.5:
#     print('过轻')
# elif 18.5<BMI<=25:
#     print('正常')
# elif 25<BMI<28:
#     print('过重')
# elif 28<BMI<=32:
#     print('肥胖')
# else :
#     print('严重肥胖')
######## for 循环
#Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：
#eg
# sum = 0
#for x in range(101): #range 函数 产生一定范围的数字
#     sum = sum + x
# print(sum)
#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现
#eg
# sum = 0
# n = 100
# while n > 0:
#     sum = sum + n
#     n = n - 1
# print(sum)
#请利用循环依次对list中的每个名字打印出Hello, xxx!：
# L = ['Bart', 'Lisa', 'Adam']
# for B in L :
#     print('Hello,',B,'!')
#     print("Hello, %s!" % B)
