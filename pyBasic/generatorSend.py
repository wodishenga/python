#A.通过g.send(None)或者next(g)可以启动生成器函数，并执行到第一个yield语句结束的位置。此时，执行完了yield语句
#，但是没有给receive赋值。yield value会输出初始值0.注意：在启动生成器函数时只能send(None),如果试图输入其它的值都会得到错误提示信息。
#B.通过g.send(‘aaa’)，会传入aaa，并赋值给receive，然后计算出value的值，并回到while头部，执行yield value语句有停止。此时yield value会输出”got: aaa”，然后挂起。
#通过g.send(3)，会重复第2步，最后输出结果为”got: 3″
#C. 当我们g.send(‘e’)时，程序会执行break然后推出循环，最后整个函数执行完毕，所以会得到StopIteration异常。

def gen():
	value = 0
	while True:
		receive = yield value
		if receive == 'e':
			break
		value = 'got:%s' % receive


g = gen()

print(g.send(None)) #0
print(g.send('aaa')) #got:aaa
print(g.send(3))    #got:3
print(g.send('e'))  #stopIneration
