# #####提取固定时间的 日志文件
# import time
# ##创建9点和12点的9元组时间对象
# t9 = time.strptime('2019-05-15 09:00:00', '%Y-%m-%d %H:%M:%S')
#
# t12 = time.strptime('2019-05-15 12:00:00', '%Y-%m-%d %H:%M:%S')
#
# ###实现 :读取文件的每一行,取出前19个字符转换9元组列表
# #若时间在t9和t12之间,则打印
# with open('myfile.txt') as fobj:
#     for line in fobj:
#         t = time.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
#         if t9 < t < t12:
#             print(line, end='')

#########改进写法,通过先对大于t12的部分的剔除,来减少判断
#####使用 time模块实现
# import time
# t9 = time.strptime('2019-05-15 09:00:00', '%Y-%m-%d %H:%M:%S')
#
# t12 = time.strptime('2019-05-15 12:00:00', '%Y-%m-%d %H:%M:%S')
# with open('myfile.txt') as fobj:
#     for line in fobj:
#         t = time.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
#         if t > t12:
#             break
#         if t > t9:
#             print(line, end='')




####################使用datetime 模块  模块位置 datetime.datetime.strptime--
import datetime

t9 = datetime.datetime.strptime('2019-05-15 09:00:00', '%Y-%m-%d %H:%M:%S')

t12 = datetime.datetime.strptime('2019-05-15 12:00:00', '%Y-%m-%d %H:%M:%S')

with open('myfile.txt') as fobj:
    for line in fobj:
        t = datetime.datetime.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
        if t > t12:
            break
        if t > t9:
            print(line, end='')
