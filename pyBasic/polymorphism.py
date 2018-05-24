#coding=utf-8

class a(object):
	def show(self):
		print("i am A")

class b(a):
	def show(self):
		print("i am B")

class c(a):
	def show(self):
		print("i am C")

def func(obj):
	obj.show()

A = a()
B = b()
C = c()

func(A)
func(B)
func(C)

