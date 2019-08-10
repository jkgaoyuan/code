from dbconn import Departments, Employees, Session
session = Session()
#########插入
# hr = Departments(dep_id=1, dep_name='人事部')
# ops = Departments(dep_id=2, dep_name='运维部')
# dev = Departments(dep_id=3, dep_name='开发部')
# qa = Departments(dep_id=4, dep_name='测试部')
# sales = Departments(dep_id=5, dep_name='销售部')
# market = Departments(dep_id=6, dep_name='市场部')
# session.add_all([hr, ops, dev, qa, sales, market])

#######################################
##增加员工
# lb = Employees(
#     emp_id=1, emp_name='刘备',
#     birth_date='1975-03-18', email='lb@qq.com', dep_id=1
# )
# gy = Employees(
#     emp_id=2, emp_name='关羽',
#     birth_date='1980-2-15', email='gy@qq.com', dep_id=2
# )
# zf = Employees(
#     emp_id=3, emp_name='张飞',
#     birth_date='1982-10-3', email='zf@qq.com', dep_id=2
# )
# zy = Employees(
#     emp_id=4, emp_name='赵云',
#     birth_date='1995-4-19', email='zy@163.com', dep_id=2
# )
# hz = Employees(
#     emp_id=5, emp_name='黄忠',
#     birth_date='1970-1-1', email='hz@126.com', dep_id=3
# )
# wy = Employees(
#     emp_id=6, emp_name='魏严',
#     birth_date='1993-6-13', email='wy@163.com', dep_id=3
# )
#
# session.add_all([lb, gy, zf, zy, hz, wy])

##########查询
###
# qset1 = session.query(Departments)
# for dep in qset1:
#     print(dep.dep_id, dep.dep_name)
#
# qset2 = session.query(Departments.dep_id, Departments.dep_name)
# for dep in qset2:
#     print(dep)

####排序
# qset3 = session.query(Departments).order_by(Departments.dep_id)
# for dep in qset3:
#     print(dep.dep_id, dep.dep_name)
# print('*' * 30)
#
# for dep in qset3[2:5]:
#     print(dep.dep_id, dep.dep_name)
#
# qset4 = session.query(Departments).filter(Departments.dep_id >=3)
# for dep in qset4:
#     print(dep.dep_id, dep.dep_name)
# print('*' * 30)
# qset5 = session.query(Departments).filter(Departments.dep_id >=3)\
#     .filter(Departments.dep_id < 6)  ###写在一行会报错
# for dep in qset5:
#     print(dep.dep_id, dep.dep_name)
# qset6 = session.query(Departments).filter(Departments.dep_id.in_([1, 3]))
# for dep in qset6:
#     print(dep.dep_id, dep.dep_name)
# qset7 = session.query(Employees).filter(Employees.email.like('%@qq.com'))
# for emp in qset7:
#     print(emp.emp_name, emp.email)
#
# qset8 = session.query(Departments.dep_id, Departments.dep_name)
# print(qset8)        # qset8是SQL语句
# print(qset8.all())      # all方法返回列表
# print(qset8.first())   # first返回all中的第一项
# qset9 = session.query(Departments.dep_id,Departments.dep_name)\
#     .filter(Departments.dep_id==6)
# # one方法要求查询的结果只有一项，0或多项都报错
# print(qset9.one())
qset10 = session.query(Employees.dep_id, Departments.dep_name)\
    .join(Departments)
print(qset10.all())
qset11 = session.query(Departments).filter(Departments.dep_name=='人事部')
hr = qset11.one()
hr.dep_name = '人力资源部'
qset12 = session.query(Departments).filter(Departments.dep_id==6)
sales = qset12.one()
session.delete(sales)
################
session.commit()
session.close()
