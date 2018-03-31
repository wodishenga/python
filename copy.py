
from multiprocessing import Pool, Manager
import os

def filesCopy(name, oldFolderName, newFolderName, queue):
	filename = oldFolderName+"/"+name
	if(os.path.getsize(filename)):
		fread = open(oldFolderName+"/"+name)
		fwrite = open(newFolderName+"/"+name, "w")
		while True:
			content = fread.read(1024)
			if len(content) == 0:
				break
  			fwrite.write(content)

		fread.close()
        fwrite.close()

        queue.put(name)
    else:
 		print("文件为空不拷贝了")


def main():

	#获取文件夹名字
	oldFolderName = input("请输入你要拷贝的文件夹:")
	print(oldFolderName)

	#创建一个新文件夹
	newFolderName = oldFolderName + ["-附件"]

	#创建新文件夹
	os.mkdir(newFolderName)

	#获取文件夹中的所有名字
	filesName = os.listdir(oldFolderName)

	#使用多进程拷贝
	pool = Pool(5)
	queue = Manager().Queue()

	for name in filesName:
		pool.apply_async(filesCopy, (name, oldFolderName, newFolderName, queue, ))

	#显示进度
	num = 0
	allNum = len(filesName)
	while num < allNum:
		queue.get_nowait()
		num+=1
		copyRate = num/allNum
		print("\rcopy的进度是：%.2f%%"%(copyRate*100), end="")

	pool.close()
	pool.join()
if __name__ == "__main__":
	main()






