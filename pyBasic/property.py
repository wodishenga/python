#coding=utf-8
class Money(object):
	"""通过设置property属性可以在类的外部设置和访问对象的私有属性"""
	def __init__(self):
		self.__money=0

	def getMoney(self):
		return self.__money

	def setMoney(self, value):
		if isinstance(value, int):
			self.__money = value
		else:
			print("error input")
	money = property(getMoney,setMoney)


a = Money()
print(a.money) #0
a.money = 100
print(a.money) #100
print(a.getMoney()) #100
