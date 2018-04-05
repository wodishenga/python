from socket import *
from threading import Thread

udpSocket = None
destIp = ""
destPort = 0
#1.接收数据
def recvData():
	while True:
		recvdata = udpSocket.recvfrom(1024)
		print("<<:%s,%s"%(recvData[1], recvData[0]))
	

#2.发送数据
def sendData():
	while True:
		senddata = input(">>")
		udpSocket.sendto(senddata.encode("utf-8"), (destIp, destPort))


#3.主函数，创建socket和发送和接收线程
def main():
	global udpSocket
	global destIp
	global destPort


	destIp = input("请输入对方的IP地址：")
	destPort = int(input("请输入对方的端口号："))	
	localPort = int(input("请输入本端的端口号；"))
	#创建socket
	udpSocket = socket(AF_INET, SOCK_DGRAM)
	#绑定本地端口
	udpSocket.bind(("", localPort))

	#创建两个线程处理发送和接收数据
	recvThread = Thread(target=recvData)
	sendThread = Thread(target=sendData)

	recvThread.start()
	sendThread.start()

	recvThread.join()
	sendThread.join()

if __name__ == "__main__":
	main()
