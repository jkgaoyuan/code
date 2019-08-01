
# for i in range(3):
#     for v in range(i + 1 ):
#         print('hello',end= ' ')
#     print()
#
# for i in range(1,10): #行
#     for v in range(1,i + 1): #列
#         print('%sx%s=%s' % (v,i, i * v),end = ' ') # end = ' '将输出时的回车,变为 空格
#     print()
#     *      1     0 1 2 3 4
#    ***     3
#   *****    5
#  *******   7    * 2i-1   空格0


#输出192.168.1.0/24 网段的所有ip
#print(['192.168.1.%s' % i for i in range(0,256)])
#输出一个等腰三角形
n = int(input('行数'))
for i in range(n):
    for j in range(0,n-i):
        print('',end=' ')
    for k in range(n - i,n):
        print('*',end=' ')
    print('')