####使用lambda 匿名函数;来简化 逻辑结构
###目的是产生10个随机数 输出大于50的数字
from random import randint
nums = [randint(1, 100) for i in range(10)]
print(nums)
def fun1(x):
    return True if x < 50 else False ###三元表达式
print(list(filter(fun1, nums)))

print(list(filter(lambda x:True if x < 50 else False, nums)))


#############
####    map 函数 ####
###map(fun1, nums)
###第一个参数是函数
###第二个参数是序列,序列中的每个对象 作为前面函数的参数

def fun2(x):
    return x * 2
print(list(map(fun2, nums)))

print(list(map(lambda x: x * 2,nums)))



#############阶乘

def func(x):
    if x == 1:
        return 1
    return x * func(x -1 )

print(func(5))