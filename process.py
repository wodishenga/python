from multiprocessing import Process

import os
import time

class Process_Class(Process):

	def __init__(self, interval):
		Process.__init__(self)
		self.interval = interval

	def run(self):
		"""redefine the run func ,when the process use the start() func ,and it will be called"""
		print("child start process id = %d"%os.getpid())
		time_start = time.time()
		time.sleep(self.interval)
		time_end = time.time()
		print("child end %d, and it costs %d seconds"%(os.getpid(), time_end-time_start))

if __name__ == "__main__":
	t_start = time.time()
	print("The main process(%d)"%os.getpid())
	p = Process_Class(2)
	p.start()
	p.join()
	t_end = time.time()
	print("mian process over, it cost %d second"%(t_end-t_start))


