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
# #
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
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# B = L[0]
# print(B[0])
print(L[0][0],L[1][1],L[-1][-1])
