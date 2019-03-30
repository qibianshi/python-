import socket


def send_message(tcp_socket):
	pass
	send_data = input("请输入您要发送的内容：")
	tcp_socket.send(send_data.encode("utf-8"))


def receive_message(tcp_socket):
	pass


def main():
	"""客户端主函数"""
	# 创建套接字
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# 建立链接
	# tcp_socket.connect(("10.63.13.61", 8080))
	dest_ip = input("请输入目标ip地址：")
	dest_port = input("请输入目标端口：")
	tcp_socket.connect((dest_ip, int(dest_port)))
	# 发送数据
	send_message(tcp_socket)

	# 接收数据
	receive_message(tcp_socket)
	# 关闭套接字
	tcp_socket.close()


if __name__ == "__main__":
	main()