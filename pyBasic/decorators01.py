
def decorators(func):
	"""普通装饰器"""
	print("----excute decorating----")
	def inner():
		print('正在进行验证')
		func()
	return inner
#只要python解释器执行到了这里，那么python解释器就会自动调用装饰器进行装饰，而不是等到被装饰的函数调用时才进行装饰
@decorators          #这里相当于执行了  f1= decorators(f1)  f1指向了inner函数
def f1():
	print("----f1------")

@decorators
def f2():
	print("----f2-----")


f1()

f2()
"""
----excute decorating----
----excute decorating----
正在进行验证
----f1------
正在进行验证
----f2-----
"""
