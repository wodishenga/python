from multiprocessing import Pool, Manager

import os, time, random

def readr(q):
	print("reader, zi = %d, fu = %d"%(os.getpid(), os.getppid()))
	for i in range(q.qsize()):
		print("reader get message:%s"%(q.get()))

def writer(q):
	print("writer:zi=%d, fu=%d"%(os.getpid(), os.getppid()))
	for i in "donge":
		q.put(i)

if __name__ == "__main__":
	print("main process start:%d"%os.getpid())
	q = Manager().Queue() #使⽤Manager中的Queue来初始化
	po = Pool()
	po.apply(writer, (q, ))
	po.apply(readr, (q, ))
	po.close()
	po.join()
	print("main process :%d"%os.getpid())


