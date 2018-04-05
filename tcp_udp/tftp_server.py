#coding=utf-8
from socket import *
import struct

udpSocket = socket(AF_INET, SOCK_DGRAM)

ipaddr = ("", 6655)
udpSocket.bind(ipaddr)

sendSeq = 0
while True:
	#接收请求
	recvData, recvAddr = udpSocket.recvfrom(1024)

	#看是什么类型的数据
	req = struct.unpack("!HH", recvData[:4])
	print(req[0])
	if req[0] == 1:  #请求数据
		try:
			f = open("test.txt", "r")
			while True:
				sendData = f.read(512)
				print("1")
				sendDataLen = len(sendData)
				sendSeq += 1
				if sendDataLen == 512:	
					sendPackge = struct.pack("!HH512s", 3, sendSeq, sendData)
				else:
					strInfo = "!HH"+str(sendDataLen)+"s"
					sendPackge = struct.pack(strInfo, 3, sendSeq, sendData)
				print("发送第%d次数据"%sendSeq);
				udpSocket.sendto(sendPackge, recvAddr)
				print("3")
				recvData, recvAddr = udpSocket.recvfrom(1024)
				recvAck = struct.unpack("!HH", recvData[:4])
				if sendDataLen < 512:
					f.close()
					sendSeq = 0
					print("文件发送完毕")
					break
				if recvAck[0] == 4 and recvAck[1] == sendSeq:
					continue
		except Exception as result:
			print("file not exist error")
			exit()
		
	else:
		print("对不起，目前我们还不支持上传")

