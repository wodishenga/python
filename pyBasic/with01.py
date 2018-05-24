#coding=utf-8
#with语法
class Sample():
	def __enter__(self):
		print("In__enter__")
		return "foo"
	def __exit__(self,type, value,trace):
		print("In__exit__")

def getSample():
	return Sample()

with getSample() as sample:
	print(sample)

#with 后面的语句被求值后,返回对象的__enter__方法被调用，这个方法的返回值将赋值给as后面的变量,当with 后面的代码全部执行完毕后,将调用前面返回对象的__exit__方法
"""
In__enter__
foo
In__exit__
"""
