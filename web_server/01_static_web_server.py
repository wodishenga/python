from socket import *
from multiprocessing import Process
import re

documentRoot = "./"

def func(clientSocket):
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
    serverSocket = socket(AF_INET, SOCK_STREAM)
    #端口复用
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    ipaddr = ("127.0.0.1", 8000)
    serverSocket.bind(ipaddr)
    serverSocket.listen(10)
    try:
        while True:
            clientScoket, clientAddr = serverSocket.accept()
            print("有客户端接入")
            p = Process(target=func, args=(clientScoket, ))
            p.start()
            #关掉父进程中复制的socket
            clientScoket.close()
    finally:
        serverSocket.close()

if __name__ == "__main__":
    main()
