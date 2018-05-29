
def Genericdecorators(func):
	"""通用装饰器"""
	print("----excute decorating----")
	def inner(*args, **kwargs):
		print("---日志记录---")
		ret = func(*args, **kwargs)
		return ret
	return inner

@Genericdecorators
def f1():
	print("----test---")
	return "f1"

@Genericdecorators
def f2(a,b,c):
	result = a+b+c
	return result

a = f1()
print(a)

b = f2(1,2,3)
print(b)
"""
----excute decorating----
----excute decorating----
---日志记录---
----test---
f1
---日志记录---
6

"""
