#coding=utf-8

#with 跳过异常
class Sample:
	def __enter__(self):
		return self
	def __exit__(self, type, value, trace):
		print(value)
		return isinstance(value,ZeroDivisionError)
	def do_something(self):
		bar = 1/0
		return bar + 10
with Sample() as sample:
	sample.do_something()
	print("pass")


#只要让这个__exit__返回true即可,注意不会调用异常出现之后的语句，也就是说不会打印pass
