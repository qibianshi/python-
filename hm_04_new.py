import socket


def send_message(udp_socket):
	dest_ip = input("请输入对方的ip地址：")
	dest_port = input("请输入对方的端口：")
	while True:
		print("返回上一级请按[0]")
		message = input("请输入要发送的信息：")
		if message == "0":
			break
		udp_socket.sendto(message.encode("utf-8"), (dest_ip, int(dest_port)))


def receive_message(udp_socket):
	# 绑定端口
	udp_socket.bind("", 9527)
	# 接收信息
	recv_message = udp_socket.recvfrom(1024)
	print("%s:%s", (recv_message[1], recv_message[0].decode("gbk")))


def main():

	# 提示信息
	print("发送数据[1]")
	print("接收数据[2]")
	print("退出程序[0]")
	press = input("请输入您要进行的操作：")

	# 创建套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	if press == "1": 
		# 发送数据
		send_message(udp_socket)
	elif press == "2":
		# 接收数据
		receive_message(udp_socket)
	elif press == "0":
		return
	else:
		print("输入有误，请重新输入！")
	# 关闭套接字
	udp_socket.close()


if __name__ == "__main__":
	main()
