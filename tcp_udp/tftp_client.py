#coding=utf-8
from socket import *
import struct
import sys
# 命令行处理
if (len(sys.argv) != 2):
	print('-'*30)
	print("tips:")
	print("python xxxx.py 192.168.0.128")
	print('-'*30)
	exit()
else:
	ip = sys.argv[1]

seqNum = 0
# 构造读请求，并向服务器发送
# 1.创建socket
udpSocket = socket(AF_INET, SOCK_DGRAM)
# 2.构造读请求(H代表两个字节，8s代表文件的长度，b代表一个字节)
sendReq = struct.pack("!H8sb5sb",1,b"test.jpg",0,b"octet",0)
# 3.发送请求
udpSocket.sendto(sendReq, (ip, 6655))

# 接收数据
while True:
	recvData, recvAddr = udpSocket.recvfrom(1024)
	recvDataLen = len(recvData)

	cmd = struct.unpack("!HH", recvData[:4])
	recvSeqNum = cmd[1]
	if cmd[0] == 3:  # 如果是数据包
		if recvSeqNum == 1:
			file = open("test.txt", "a")
		if seqNum+1 == recvSeqNum:
			file.write(str(recvData[4:]))
			seqNum += 1
			print('(%d)次接收到的数据'%(seqNum))
			# send ACK
			sendAck = struct.pack("!HH", 4, seqNum)
			print("sendAck")
			udpSocket.sendto(sendAck, (ip, 6655))
			print("sendAck over")
			print(recvDataLen)
		if recvDataLen < 516:
			file.close()
			print("文件成功下载")
			break
	elif cmd[0] == 5:
		print("error num:%d" % seqNum)
		break

#关闭socket
udpSocket.close()



