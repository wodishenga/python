from threading import Thread
from socket import *

def clientHandle(newSocket,clientAddr):
	while True:
		recvData = newSocket.recv(1024)
		if len(recvData) > 0:
			print("recv[%s]:%s"%(str(clientAddr), recvData))
		else:
			print("[%s]客户端已经关闭")
			break
	newSocket.close()

def main():

	serverSocket = socket(AF_INET, SOCK_STREAM)
	#重复使用绑定的信息
	serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR , 1)

	Addr = ("192.168.1.128", 7788)
	serverSocket.bind(Addr)

	serverSocket.listen(5)

	try:
		while True:
			print("等待客户端接入----")
			newSocket,clientAddr = setsockopt.accept()
			print("主进程，，接下来创建一个新的线程负责数据处理")
			pClient = Thread(target=clientHandle, args=(newSocket, clientAddr, ))
			pClient.start()

			#注意这里不要关闭newsocket了，因为这里线程共享主进程创建的socket
			#newSocket.close()
	finally:
		#当为所有的客户端服务完之后再进⾏关闭，表示不再接收新的客户端的链接
		serverSocket.close()

if __name__ == "__main__":
	main()

