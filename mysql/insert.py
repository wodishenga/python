# coding=utf-8

from MySQLdb import *

try:
    # name = raw_input("请输入名字 :")
    # name2 = raw_input("请输入名字 :")
    #生成一个连接数据库的对象
    conn = connect(host="localhost", port=3306, user="root", passwd="a", db="python3", charset="utf8")
    #用连接对象返回一个对象cursor1用于对数据库的修改等操作
    cursor1 = conn.cursor()
    #1.curd
    #sql = 'insert into class(name) values("zhushengjie")' #注意这里一定要用单引号
    #sql = ' update  class set name="haha" where id =4'
    # cursor1.execute(sql)

    #2.参数化
    #sql = 'insert into class(name) values(%s), (%s)'  #%s只是个占位符，可以是任意数据,
    #执行sql语句
    #cursor1.execute(sql, [name, name2])    #注意name放到一个列表中

    #3.查询
    sql =  'select * from students'
    cursor1.execute(sql)
    # 查询一条数据
    #result = cursor1.fetchone()
    #查询多条数据
    result = cursor1.fetchall()
    print(result)
    #提交
    conn.commit()

    cursor1.close()
    conn.close()
except Exception, e:
    print(e.message)

