import pymysql

# 建立连接
conn = pymysql.connect(
    host='192.168.1.58',
    port=3306,
    user='gaoyuan',
    passwd='gaoyuan',
    db='nsd1903',
    charset='utf8'
)

# 创建操作数据库的游标
cursor = conn.cursor()
################### 插入数据
# insert = "INSERT INTO departments VALUES(%s, %s)"
# deps = [(1, '人事部'), (2, '运维部'), (3, '开发部'), (4, '测试部'),(5, '市场部'),(6, '销售部')]
# cursor.executemany(insert, deps)
# conn.commit()
# cursor.close()
############################
#######查询
# select = "SELECT * FROM departments"
# cursor.execute(select)  ####游标
# result1 = cursor.fetchone()
# print(result1)
# print('*' * 30)
# result2 = cursor.fetchmany()
# print(result2)
# print('*' * 30)
# result3 = cursor.fetchall()
# print(result3)

##########移动游标
# select = "SELECT * FROM departments ORDER BY dep_id"
# cursor.execute(select)
# cursor.scroll(2, mode='absolute') ####绝对移动从开头移动2个记录
# result1 = cursor.fetchone()
# print(result1)
# print('*' * 30)
# cursor.scroll(1)  ###相对移动2
# result2 = cursor.fetchone()
# print(result2)

###############3修改
update = "UPDATE departments SET dep_name=%s WHERE dep_name=%s"
data = ('人力资源部', '人事部')
cursor.execute(update, data)

##########删除
# delete = "DELETE FROM departments WHERE dep_id=%s"
# dep = (6,)
# cursor.execute(delete, dep)