import socket


def receive_data(down_file_name, tcp_client_socket):
    """接收数据函数"""
    recv_data = tcp_client_socket.recv(1024)
    with open("[new]" + down_file_name, "wb") as f:
        f.write(recv_data)


def main():
    """tcp客户端主函数"""
    # 创建套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 获取服务器的ip地址和port号
    dest_ip = input("请输入目标服务器的ip地址：")
    dest_port = int(input("请输入目标 服务器的port号："))

    # 链接服务器
    tcp_client_socket.connect((dest_ip, dest_port))
    # 发送需要下载的文件名
    download_file_name = input("请输入需要下载的文件名：")
    tcp_client_socket.send(download_file_name.encode("utf-8"))
    # 接收服务器返送回来的数据
    receive_data(download_file_name)
    # 关闭套接字
    tcp_client_socket.close()


if __name__ == "__main__":
    main()
