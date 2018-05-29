

def decorators(func):
	"""用装饰器对有参数的函数进行装饰"""
	print("----excute decorating----")
	def inner(a,b):
		print("---2---")
		func(a,b)
		print("---3---")
	print("---1---")
	return inner

@decorators
def fun(a,b):
	print("a+b = %d"%(a+b))	


fun(10,20)
"""
----excute decorating----
---1---
---2---
a+b = 30
---3---
"""
