#在一个生成器中，如果没有return，则默认执行到函数完毕时返回StopIteration；
#如果遇到return,如果在执行过程中 return，则直接抛出 StopIteration 终止迭代
#如果在return后返回一个值，那么这个值为StopIteration异常的说明，不是程序的返回值。生成器没有办法使用return来返回值
def func():
	yield 'a'
	return 
	yield 'b'


f = func()
print(next(f)) #a

next(f)  #抛出异常
