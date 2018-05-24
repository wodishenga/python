#coding=utf-8

class test(object):
	num = 0
	def __init__(self):
		#实例属性
		self.name = "dj"
	#类方法
	@classmethod
	def addNum(cls):
		cls.num+=1
		print(cls.num)
	#静态方法
	@staticmethod
	def printInfo():
		print("我是你爸爸")

a = test()

b = test()

a.addNum() #1
b.addNum() #2
test.addNum() #3

a.printInfo()
test.printInfo()
