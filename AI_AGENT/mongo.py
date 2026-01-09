import pymongo
import uuid
client = pymongo.MongoClient("mongodb://localhost:27017")  #链接的数据库
rg_user =  client['rg_user']  #创建数据库
user = rg_user['users']   #创建数据库中的集合

todo1 = {'_id':'1','name':'A','gender':'m'}
todo2 = {'_id':'12','name':'B','gender':'f'}
#使用inster one 插入数据库
user.insert_one(todo1)
user.insert_one(todo2)