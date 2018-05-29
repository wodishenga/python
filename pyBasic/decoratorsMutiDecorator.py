#多个装饰器
def decorators1(func):
	def inner():
		print("-----1----")
		return "<b>" + func() + "</b>"
	return inner

def decorators2(func):
	def inner():
		print("----2----")
		return "<h4>"+func()+"</h4>"
	return inner

@decorators1
@decorators2
def test():
	print("----3----")
	return "hello my king"

ret = test()
print(ret)

"""
-----1----
----2----
----3----
<b><h4>hello my king</h4></b>
"""
