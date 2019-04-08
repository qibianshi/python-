from collections import Iterable


class Classmate(object):

	def __init__(self):
		self.names = list()

	def add(self, name):
		self.names.append(name)

	def __iter__(self):
		return ClassIterator(self)


class ClassIterator(object):

	def __init__(self, obj):
		self.obj = obj

	def __iter__(self):
		pass

	def __next__(self):
		return self.obj.names[0]
		
classmate = Classmate()
classmate.add("张三")
classmate.add("李四")
classmate.add("王五")

print("判断classmate是否是可以迭代的对象", isinstance(classmate, Iterable))

iter(classmate)
