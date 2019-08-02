# #用户指定长度的斐波那契数列
# def gen_fib():
#     alist = [0,1]
#     s1 = 0
#     num = int(input('输入长度:'))
#     for i in range(num - 2):
#
#         alist.append(alist[-1] + alist[-2])
#
#     print(alist)
#
# gen_fib()


###函数调用
def gen_fib(n):
    fib = [0,1]
    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib
mylist = [5,8,10,7,13]
for i in mylist:
    print(gen_fib(i))
a = int(input('leng:'))

result = gen_fib(a)

print(result)