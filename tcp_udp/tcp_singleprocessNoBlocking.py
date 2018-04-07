from socket import *

#用来存贮客户端信息
clientSocketList = []
def main():

	serverSocket = socket(AF_INET, SOCK_STREAM)
	#重复使用绑定的信息
	serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR , 1)

	Addr = ("192.168.1.128", 7788)
	serverSocket.bind(Addr)

	serverSocket.listen(5)

	#设置非阻塞套接字
	##将套接字设置为⾮堵塞
	#设置为非堵塞后，如果accept时，恰巧没有客户端connect，那么accept会产生一个异常，所以需要try来进行处理
	serverSocket.setblocking(False)

	while True:
		try:
			clientSocket,clientAddr = serverSocket.accept()

		except:
			pass #如果没有客户端连接，accept触发异常，什么都不做,如果没有异常则进行客户端处理
		else:
			print("一个新客户端到来:%s"%str(clientAddr))
			clientSocket.setblocking(False) 
			clientSocketList.append((clientSocket,clientAddr))
			#轮询检查客户端是否有数据接收
			for clientSocket,clientAddr in clientSocketList:
				try:
					recvData = clientSocket.recv(1024) #没有接收到数据会触发异常，处理时什么都不做
				except:
					pass
				else:
					if len(recvData) > 0:
						print("%s:%s"%(str(clientAddr), recvData))
					else:
						clientSocket.close()
						clientSocketList.remove((clientSocket,clientAddr))
						print("%s已经下线"%str(clientAddr))

if __name__ == "__main__":
	main()

