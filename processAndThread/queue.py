from multiprocessing import Process, Queue

import os,time,random


def writer(q):
	for value in ["a", "b", "c"]:
		print("put %s to the queue"%value)
		q.put(value)
		time.sleep(random.random())

def reader(q):
	while True:
		if not q.empty():
			value = q.get()
			print("get %s from the queue"%value)
			time.sleep(random.random())
		else:
			break

if __name__ == "__main__":
	q = Queue()
	P1 = Process(target=writer,args=(q, ))
	P2 = Process(target=reader,args=(q, ))

	P1.start()
	P1.join()

	P2.start()
	P2.join()







