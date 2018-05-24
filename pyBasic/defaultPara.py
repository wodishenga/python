#coding=utf-8

def etlist(val, list=[]):
	list.append(val)
	print(id(list))
	print('list=%s'%list)
	return list

list1 = etlist(10)
list2 = etlist(123,['a','b', 'c'])
list3 = etlist('a')

print 'list1 = %s' %list1
print 'list2 = %s' %list2
print 'list3 = %s' %list3

"""
140694804748048
list=[10]
140694804758184
list=['a', 'b', 'c', 123]
140694804748048
list=[10, 'a']
list1 = [10, 'a']
list2 = ['a', 'b', 'c', 123]
list3 = [10, 'a']
#默认列表只在函数被定义的那一刻创建一次,也就是说list1和list3是同一个列表，而list2是自带了一个自己的列表
"""
print("-------------------")
def etlist2(val,list2=None):
	if list2 == None:
		list2 = []
		list2.append(val)
	return list2


list1 = etlist2(10)
list2 = etlist2(123,['a','b', 'c'])
list3 = etlist2('a')
print 'list1 = %s' %list1
print 'list2 = %s' %list2
print 'list3 = %s' %list3

"""
list1 = [10]
list2 = ['a', 'b', 'c']
list3 = ['a']
"""
