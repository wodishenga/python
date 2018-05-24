#coding=utf-8
#with 异常处理
class Sample():
	def __enter__(self):
		return self
	def __exit__(self, type, value,trace):
		print(type)
		print(value)
		print(trace)
	def do_something(self):
		bar = 1/0
		return bar + 10

with Sample() as sample:
	sample.do_something()
#在with后面的代码块抛出任何异常时，__exit__() 方法被执行
"""
type: <type 'exceptions.ZeroDivisionError'>
value: integer division or modulo by zero
trace: <traceback object at 0x1004a8128>
Traceback (most recent call last):
  File "./with_example02.py", line 19, in <module>
    sample.do_something()
  File "./with_example02.py", line 15, in do_something
    bar = 1/0
ZeroDivisionError: integer division or modulo by zero
"""
