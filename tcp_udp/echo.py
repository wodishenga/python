from socket import *

def main():
	#创建socket
	udpSocket = socket(AF_INET, SOCK_DGRAM)

	#绑定端口号
	udpSocket.bind(("", 7788))

	while True:
		#接受来自各端口号的数据
		recvData = udpSocket.recvfrom(1024)
		content,destInfo = recvData

		print(destInfo, end="")
		print(":%s"%content.decode("gb2312"))

if __name__ == "__main__":
	main()
