from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

udpSocket.bind(("", 7788))

sendData = "你好啊"
#python3以gb2312格式对发送数据进行编码
udpSocket.sendto(sendData.encode("gb2312"),("192.168.0.103", 8080))

receData = udpSocket.recvfrom(1024)

content, destInfo = receData
#对接收数据进行解码
print("received data is %s"%content.decode("gb2312"))
print(destInfo)


