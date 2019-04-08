def creat_num(all_num):
	a, b = 0, 1
	current_num = 0
	while current_num < all_num:
		yield a
		a, b = b, a+b
		current_num += 1


obj = creat_num(10)

# ret = next(obj)
# print(ret)

# ret = next(obj)
# print(ret)
# ret = next(obj)
# print(ret)
# ret = next(obj)
# print(ret)
# ret = next(obj)
# print(ret)


for num in obj:
	print(num)

