# coding=utf-8

from redis import *

try:
    r = StrictRedis(host="127.0.0.1", port=6379)
except Exception,e:
    print e.message

#写
#缓冲多条命令，然后一次性执行，减少服务器-客户端之间TCP数据库包，从而提高效率
pipe = r.pipeline()
pipe.set("py10", "hello")
pipe.set("py11", "world")
pipe.execute()


class redisHelper:
    def __init__(self, host, port):
        self.__redis = StrictRedis(host, port)

    def set(self, key, value):
        self.__redis.set(key, value)

    def get(self,key):
        return self.__redis.get(key)

