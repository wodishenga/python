from socket import *
from multiprocessing import Process
import re

# 设置静态文件根目录
documentRoot = "./"


class HttpServer(object):
    """"""

    def __init__(self, port):
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        # 端口复用
        self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        ipaddr = ("127.0.0.1", port)
        self.serverSocket.bind(ipaddr)
        # serverSocket.listen(10)

    def Start(self):
        self.serverSocket.listen(10)
        while True:
            clientScoket, clientAddr = self.serverSocket.accept()
            print("有客户端接入")
            p = Process(target=self.handleClient, args=(clientScoket,))
            p.start()
            # 关掉父进程中复制的socket
            clientScoket.close()

    def handleClient(self, clientSocket):
        recvData = clientSocket.recv(1024)
        requestHeadLines = recvData.splitlines()
        for i in requestHeadLines:
            print(i)
        httpRequestMethodLine = requestHeadLines[0]
        getFileName = re.search("(/.*?)HTTP", httpRequestMethodLine.decode("utf-8")).group(1)
        print("file	name	is	===>%s" % getFileName)
        if getFileName == '/':
            getFileName = documentRoot + "index.html"
        else:
            getFileName = documentRoot + getFileName
        print("file	name	is	===2>%s" % getFileName)  # for	test

        try:
            f = open(getFileName)
        except IOError:
            responseHeaderLines = "HTTP/1.1	404	not	found\r\n"
            responseHeaderLines += "\r\n"
            responseBody = "====sorry	,file	not	found===="
        else:
            responseHeaderLines = "HTTP/1.1	200	OK\r\n"
            responseHeaderLines += "\r\n"
            responseBody = f.read()
            f.close()
        finally:
            response = responseHeaderLines + responseBody
            clientSocket.send(response.encode("utf-8"))
            clientSocket.close()


def main():
    httpServer = HttpServer()
    httpServer.Start()


if __name__ == "__main__":
    main()
