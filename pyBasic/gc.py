import gc
import time

class A(object):
	def __init__(self):
		 print('object born,id:%s'%str(hex(id(self))))
	def __del__(self):
		print('object del,id:%s'%str(hex(id(self))))

def func():
	print("----0----")
	print(gc.collect())    #一开始返回0
	c1 = A()
	c2 = A()
	c1.t = c2
	c2.t = c1
	print("----1----")
	del c1
	del c2
	print(globals())
	print("----2----")
	print(gc.garbage)#没有收垃圾，是一个空列表
	print("----3----")
	print(gc.collect())#显式执行垃圾回收，返回回收垃圾的个数
	print("----4----")
	print(gc.garbage))#垃圾回收到垃圾堆里
	print("----5----")
	time.sleep(1)

if __name__ == '__main__':
	gc.set_debug(gc.DEBUG_LEAK) #设置gc模块的日志
	func()
