#coding=utf-8

class  ShortInputException(Exception):
	"""自定义异常"""
	def __init__(self, length, atleast):
		self.length = length
		self.atleast = atleast

	def __str__(self):
		msg = "你输入的长度是"+str(self.length) +",但是长度至少要"+str(self.atleast)
		return msg

def main():
	try:
		string = input("请输入一个字符串：")
		if len(string) < 5:
			raise ShortInputException(len(string), 5) #创建了一个ShortInputException异常对象，并对这个对象进行了初始化

	except ShortInputException as result: #result用于创建一个ShortInputException对象，这个result就相当于一个对象
		print(result)

	else:
		print("No problem")


main()










