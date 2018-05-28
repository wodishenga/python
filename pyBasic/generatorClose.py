#手动关闭生成器函数，后面的调用会直接返回StopIteration异常

def func():
	yield 1
	yield 2
	yield 3
g = func()

print(next(g)) #1

g.close()

print(next(g)) #抛出异常

