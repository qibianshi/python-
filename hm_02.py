from collections import Iterable
import time

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
		self.current_num = 0
	def __iter__(self):
		pass

	def __next__(self):
		if self.current_num < len(self.obj.names):
			ret = self.obj.names[self.current_num]
			self.current_num +=  1
			return ret
		else:
			raise StopIteration

classmate = Classmate()
classmate.add("张三")
classmate.add("李四")
classmate.add("王五")

print("判断classmate是否是可以迭代的对象", isinstance(classmate, Iterable))

iter(classmate)

for name in classmate:
	print(name)
	time.sleep(1)




