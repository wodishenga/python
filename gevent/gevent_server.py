#coding=utf-8
import sys
import time
import gevent
from gevent import socket,monkey
monkey.patch_all()  #能让协程自动切换，不用sleep(),且注意要用gevent自带的socket

def handle_request(conn):
	while True:
		data = conn.recv(1024) #没有数据不会等待
		if not data:
			conn.close()
			break
		print("recv:", data)
		conn.send(data)

def server(port):
	s = socket.socket()
	s.bind(('', port))
	s.listen(5)
	while True:
		cli, addr = s.accept()  #没有客户端连接，不会阻塞
		gevent.spawn(handle_request, cli)

if __name__ == '__main__':
	server(7788)
