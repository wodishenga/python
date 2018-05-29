#coding=utf-8
#1.动态地创建类
#type用于动态地创建一个类，并返回一个类对象
#class type(name, bases, dict)  name -- 类的名称。bases -- 基类的元组。dict -- 字典，类内定义的命名空间变量。
#class classFoo(object):
#	a = 1
classFoo = type("classFoo", (), {"a":1})

#instance是classFoo类创建的一个实例对象
instance = classFoo()
#a是一个类属性
print(instance.a)
print(classFoo.a)

#2.继承
def printa(self):
	print(self.a)

@staticmethod
def func():
	print("static method")
@classmethod
def func2(cls):
	print("class method")
#继承父类classFoo
classFooSon = type("classFooSon",(classFoo,), {"printa":printa, "func":func, "func2":func2})

instanceSon = classFooSon()

instanceSon.printa()
instanceSon.func()
classFooSon.func2()

#3.自定义元类
#python中所有的东西——都是对象。这包括整数、字符串、函数以及类。它们全部都是对象，而且它们都是从一个类创建而来，这个类就是type。
def upper_attr(future_class_name, future_class_parents, future_class_attrs):
	"""遍历属性，把不是__开头的属性名字变成大写"""
	newAttr = {}
	for name,values in future_class_attrs.items():
		if not name.startswith("__"):
			newAttr[name.upper()] = values
	return type(future_class_name, future_class_parents, newAttr)

#python 2
#class foo2(object):
#   __metaclass__ = upper_attr
#   bar = 'xixi'

#python3
#设置foo3类的元类为upper_attr
class foo3(object,metaclass=upper_attr):
	bar = "hehe"

print(hasattr(foo3, 'bar'))
print(hasattr(foo3,'BAR'))
t = foo3()
print(t.BAR)


#因为所有的类都是type类创建的，我们可以继承type类，改写__new__方法来实现自定义创建类
class UpperAttrMetaClass(type):
	def __new__(cls, future_class_name, future_class_parents, future_class_attrs):
		newAttr = {}
		for name,values in future_class_attrs.items():
			if not name.startswith("__"):
				newAttr[name.upper()] = values
		return type(future_class_name, future_class_parents, newAttr)
		#return type.__new__(cls,.....)
		#return super(UpperAttrMetaClass,cls).__new__(cls,......)


class foo3(object,metaclass=UpperAttrMetaClass):
        bar = "hehe"

print(hasattr(foo3, 'bar'))
print(hasattr(foo3,'BAR'))
t = foo3()
print(t.BAR)

		
	
