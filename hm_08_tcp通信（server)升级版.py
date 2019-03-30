import socket


def send_file_2_client(new_server_socket, client_addr):
    # 1.接收客户端需要下载的文件名
    file_name = new_server_socket.recv(1024).decode("utf-8")
    print("客户端(%s)要下载的文件是：%s" % (str(client_addr), file_name))
    file_content = None
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()

    except Exception as res:
        print("没有要下载的文件（%s）" % file_name)

    # 3.发送文件的数据给客户端
    if file_content:
        new_server_socket.send(file_content)


def main():
    """tcp服务器升级版"""
    # pass
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定本地ip地址
    tcp_server_socket.bind(("", 9527))
    # 让默认的套接字由主动变为被动 监听客户端 listen
    tcp_server_socket.listen(128)
    # 等待客户端的链接 accept
    new_server_socket, client_addr = tcp_server_socket.accept()
    # 调用发送文件函数,完成为客户端的服务
    while True:
        send_file_2_client(new_server_socket, client_addr)

    # 关闭套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
