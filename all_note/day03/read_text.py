# f = open('/tmp/passwd')
# data = f.read(4)
# print(data)
# #
# data = f.read(3)
# print(data)

# data = f.readline()
# print(data)

# data = f.readlines()
# print(data)

# data =  f.close()

#读取文件 for 循环方式
# f = open('/tmp/passwd')
# for i in f:
#     print(i,end='')
# f = f.close()
# print(f)
#
# f = open('/bin/ls','rb') #r 表示读 b 表示二进制
# a = f.read()
# print(a)
# f = open('/tmp/passwd','w')
# f.write('hello word!\n')
# f.flush()
# f.writelines(['2nd line\n','3rd line\n'])
# f.close()
# f = open('/tmp/passwd','rb')
# print(f.read())

##with 文件
# with open('/tmp/passwd') as f:
#     for line in f:
#         print(line,end='')

###指针移动
# f = open('/tmp/passwd','rb')
# f.tell()
# print(f.read(5))
# f.seek(0,0)
# # f.read(5)
# print(f.seek(-6,2))
# f.close()

##模拟cp 操作 拷贝/bin/ls 到指定位置
original_ls = open('/usr/bin/ls','rb')
target_ls = open('/home/student/ls','wb')
original_ls1 = original_ls.read()
print(original_ls)
target_ls.write(original_ls1)
original_ls.close()
target_ls.close()
t = open('/home/student/ls','rb')
print(t.read())
