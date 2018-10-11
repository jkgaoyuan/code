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
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''# 字符
s3 = r'Hello, "Bart"'
s4 = 'i\'m "ok"'
s5 = r'''Hello,
Lisa!'''
print(n,'\n',f,'\n',s1,'\n',s2,'\n',s3,'\n',s5,)

a = 'ABC'
b = a
a = 'pi'    #赋值 这里的运算和数学的运算是不一样的》！！！！ 这里是吧b指向a指向的字符

print(b)
print(a)
