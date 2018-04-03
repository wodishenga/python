from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

#1.绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
udpSocket.bind(("", 7788))

#2.使用udp发送的数据，每次都要加ip地址+端口号
udpSocket.sendto(b"haha", ("192.168.1.101", 8080))


##3. 等待接收对⽅发送的数据
recvData = udpSocket.recvfrom(1024)

print(recvData)

#关闭套接字
udpSocket.close()
	

