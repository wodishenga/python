# coding=utf-8

from pymongo import *

#获取客户端，建立连接
client = MongoClient("localhost", 27017)

#切换数据库
db = client.py3

#获取集合
stu = db.stu

#增加
#stu.insert_one({"name":"xixi"})

#修改
#stu.update_one({"name": "xixi"}, {"$set": {"name": "abc"}})

#删除
#stu.delete_one({"name": "abc"})

#查找
cursor = stu.find({"age": {"gt": 10}})
for s in cursor:
    print(s["name"])

