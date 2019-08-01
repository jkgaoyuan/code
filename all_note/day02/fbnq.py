#用户指定长度的斐波那契数列
alist = [0,1]
s1 = 0
num = int(input('输入长度:'))
for i in range(num - 2):

    alist.append(alist[-1] + alist[-2])

print(alist)
