# encoding=utf8
from MysqlHelper import MysqlHelper

if __name__ == "__main__":
    sql = 'select name,gender from students order by id desc'

    helper = MysqlHelper('localhost', 3306, 'python3', 'root', 'a')
    one = helper.get_one(sql)
    print one