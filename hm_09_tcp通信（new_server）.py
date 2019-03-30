import socket


def send_file(new_client_socket, client_addr):
    """文件发送函数"""
    # 获取客户端要下载的文件名
    down_file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端：[%s] 需要下载的文件是[%s]" % (client_addr, down_file_name))
    # 打开需要发送的文件并读取里面的内容
    file_content = None
    # with...as..函数是在能够确保文件存在的条件下打开相应文件，能够自动调用close函数
    # with open(down_file_name, "rb") as f:
    #     file_content = f.write(down_file_name)
    try:
        f = open(down_file_name, "rb")
        file_content = f.write()
        f.close()
    except Exception as res:
        print("没有要下载的文件：%s" % down_file_name)
    # 发送读取到的内容
    if file_content:
        new_client_socket.send(file_content)


def main():
    """tcp通信服务器"""

    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定本地ip地址
    tcp_server_socket.bind(("", 9527))
    # 将套接字 由主动变为被动监听状态 listen
    tcp_server_socket.listen(128)
    # 等待客户端的呼叫 accept
    new_client_socket, client_addr = tcp_server_socket.accept()

    # 调用文件发送函数
    send_file(new_client_socket, client_addr)
    # 关闭套接字
    new_client_socket.close()
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
