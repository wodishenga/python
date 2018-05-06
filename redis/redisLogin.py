# encoding=utf8

from MysqlHelper import MysqlHelper
from redisTest import redisHelper
from hashlib import sha1


def LoginFunc():
    # 接收用户输入
    name = raw_input("请输入用户名：")
    pwd = raw_input("请输入密码:")

    # 对密码加密
    s1 = sha1()
    s1.update(pwd)
    pwdSha1 = s1.hexdigest()

    # 先判断redis中是否存在此用户
    redis = redisHelper("localhost", 6379)
    mysql = MysqlHelper("localhost", 3306, "python3", "root", "a")
    # 判断redis中是否保存了此用户和密码
    if redis.get(name) == None:
        sql = "select upwd from userinfos where uname=%s"
        userinfo = mysql.get_one(sql, [name])
        if userinfo == None:
            print("用户名错误")
        else:
            #把mysql中查询到的数据库，存储到redis中
            redis.set(name, userinfo[0])
            if userinfo[0] == pwdSha1:
                print("成功")
            else:
                print("密码错误")
    else:
        if redis.get(name) == pwdSha1:
            print("哈哈成功")
        else:
            print("密码错误")

# 查询redis是否存在此用户

if __name__ == "__main__":
    LoginFunc()
