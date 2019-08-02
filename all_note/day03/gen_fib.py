#用户指定长度的斐波那契数列,将生成的数列每项 乘上2 在输出
# def gen_fib():
#     fib = [0,1]
#     n = int(input('输入长度:'))
#
#     for i in range(n - 2 ) :
#         fib.append(fib[-1] + fib[-2])
#     # print(fib)
#     return fib      #返回值
# nums = gen_fib()    #调运函数,函数的返回值传递给nums
# print(nums)
# nums = [i * 2 for i in nums] #和 a = a * 2 / a*=2是一个套路
# print(nums)

# #用户指定长度的斐波那契数列
def gen_fib():
    alist = [0,1]
    s1 = 0
    num = int(input('输入长度:'))
    for i in range(num - 2):

        alist.append(alist[-1] + alist[-2])

    print(alist)

gen_fib()
