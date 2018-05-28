#throw()用来向生成器函数送入一个异常，可以结束系统定义的异常，或者自定义的异常.
#A.print(next(g))：会输出normal value，并停留在yield ‘normal value 2’之前。
#B.由于执行了g.throw(ValueError)，所以会跳过所有后续的try语句，也就是说yield ‘normal value 2’不会被执行，然后进入到except语句，打印出we got ValueError here。然后再次进入到while语句部分，消耗一个yield，所以会输出normal value。
#C.print(next(g))，会执行yield ‘normal value 2’语句，并停留在执行完该语句后的位置。
#D.g.throw(TypeError)：会跳出try语句，从而print(‘here’)不会被执行，然后执行break语句，跳出while循环，然后到达程序结尾，所以跑出StopIteration异常
def gen():
	while True:
		try:
			yield 'normal value'
			yield 'normal value 2'
			print('here')
		except ValueError:
			print('we got valueError here')
		except TypeError:
			break


g = gen()
print(next(g))
print(g.throw(ValueError))
print(next(g))
print(g.throw(TypeError))
