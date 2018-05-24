#coding=utf-8

import time 


try:
	f = open("test.txt")
	try:
		while True:
			content = f.readline()
			if len(content)==0:
				break
			time.sleep(1)
			print(content)
	except:
		#ctrl+c
		pass
	finally:
		f.close()
		print("the file was closed")
except:
	print("The file does not exist")

