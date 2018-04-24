# coding:utf-8
import time
# 设置静态文件根目录
HTML_ROOT_DIR = "./static"

class Application(object):
    """框架的核心部分，也就是框架的主题程序，框架是通用的"""
    def __init__(self, urls):
        #设置路由信息
        self.urls = urls

    def __call__(self, env, start_response):
        """当调用这个类的对象同名函数时，会调用到这个函数，因此可以把这个类对象当函数用"""
        path = env.get("PATH_INFO", "/")  #获取路径，默认是/
        #/static/index.html
        if path.startswith("/static"):
            #要访问的静态文件
            file_name = path[7:]
            #打开文件，读取内容
            try:
                file = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                #代表未找到路由信息
                status = "404 Not Found"
                headers = []
                start_response(status, headers)
                return "not found"
            else:
                file_data = file.read()
                file.close()

                status = "200 0K"
                headers = []
                start_response(status, headers)
                return file_data.decode("utf-8")

        #这里只是做了一个路由转发
        for url, handler in self.urls:
            if url == path:
                return handler(env, start_response)

        ## 代表未找到路由信息，404错误
        status = "404 Not Found"
        headers = []
        start_response(status, headers)
        return "not found"


def show_ctime(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return time.ctime()


def say_hello(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return "hello haha"



#把对应的路径和相对应的函数关联起来
urls = [
    ("/", show_ctime),
    ("/ctime", show_ctime),
    ("/sayhello", say_hello)
]

#由服务器去调用这个框架，达到服务器与框架分离的效果
app = Application(urls)


