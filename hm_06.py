def creat_num(all_num):
	a, b = 0, 1
	current_num = 0
	while current_num < all_num:
		ret = yield a
		a, b = b, a+b
		print(ret)
		current_num += 1

obj = creat_num(10)

ret = next(obj)
print(ret)

ret = obj.send("hahha")
print(ret)


