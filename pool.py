from multiprocessing import Pool
import os, time, random


def worker(msg):
	t_start = time.time()
	print("pid = %d start"%os.getpid())
	time.sleep(random.random()*2)
	t_end = time.time()
	print(msg,"pid = %d over,it cost %d"%(os.getpid(),t_end-t_start)

po = Pool(3)
for i in range(10):
	#Pool.apply_async(要调用的目标，(传递给目标的参数元祖，)）
	#每次循环都会有空闲的子进程去执行目标
	po.apply_async(worker,(i,))
print("---start---")
po.close() #关闭进程池，关闭后po不再接受新的请求
po.join()  #等待所有子进程结束，必须放在close之后
print("----end---")

