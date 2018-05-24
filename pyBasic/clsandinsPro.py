#coding=utf-8

class People(object):
    country = 'china' #类属性
print(People.country)
p = People()
print(p.country)
p.country = 'japan' #（这里只是对象创建了一个同名的属性，会覆盖类属性）
print(p.country)      #实例属性会屏蔽掉同名的类属性
print(People.country)
del p.country    #删除实例属性
print(p.country)	
