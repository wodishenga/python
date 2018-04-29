# encoding=utf8

from MysqlHelper import MysqlHelper
from hashlib import sha1


def LoginFunc():
    # 接收用户输入
    sname = raw_input("请输入用户名：")
    spwd = raw_input("请输入密码:")

    # 对密码加密
    s1 = sha1()
    s1.update(spwd)
    spwdSha1 = s1.hexdigest()

    # 根据用户名查询密码
    sql = "select upwd from userinfos where uname=%s"
    params = [sname]
    sqlhelper = MysqlHelper('localhost', 3306, 'python3', 'root', 'a')
    userinfo = sqlhelper.get_one(sql, params)   #get_all  use useinfo[0][0] judge

    if userinfo == None:
        print '用户名错误'
    elif userinfo[0] == spwdSha1:
        print '登录成功'
    else:
        print '密码错误'

if __name__ == "__main__":
    LoginFunc()
