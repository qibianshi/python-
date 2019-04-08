def creat_num(all_num):
	a, b = 0, 1
	current_num = 0
	while current_num < all_num:
		yield a
		a, b = b, a+b
		current_num += 1
	# return a
	return "ok..."

obj = creat_num(10)


while True:
	try:
		ret = next(obj)
		print(ret)
	except Exception as res:
		print(res.value)
		break


