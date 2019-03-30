import socket


def main():
    """升级版客户端"""
    # pass
    # 1.创建套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.获取服务器的ip和port
    server_ip = input("请输入目标服务器的ip地址：")
    server_port = int(input("请输入目标服务器的端口："))

    # 3.建立链接
    tcp_client_socket.connect((server_ip, server_port))
    # 4.获取下载文件的名字
    download_file_name = input("请输入要下载的文件名：")
    # 5.将文件名发送到服务器
    tcp_client_socket.send(download_file_name.encode("utf-8"))
    # 6.接收文件中的数据
    recv_data = tcp_client_socket.recv(1024)

    if recv_data:
        # 7.保存接收到的数据到一个文件中
        with open("[new]" + download_file_name, "wb") as f:
            f.write(recv_data)

    # 8.关闭套接字
    tcp_client_socket.close()


if __name__ == "__main__":
    main()
