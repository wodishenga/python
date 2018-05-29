
def decoratorsArg(arg):
	def decoratorsWithParam(func):
		"""带有参数的装饰器"""
		def inner():
			print("日志记录---arg=%s"%arg)
			if arg=="one":
				func()
			else:
				func()
				func()
		return inner
	return decoratorsWithParam

@decoratorsArg("one")
def func():
	print("哈哈")

@decoratorsArg("?")
def func2():
	print("嘻嘻")


func()

func2()

"""
日志记录---arg=one
哈哈
日志记录---arg=?
嘻嘻
嘻嘻

"""


