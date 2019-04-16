import socket


def send_message(new_socket):
    """为客户端返回数据"""
    # 接收浏览器发送过来的请求，即http请求
    # GET / HTTP/1.1
    # ...
    request = new_socket.recv(1024).decode("gbk")
    print(request)
    # 返回http格式的数据给浏览器
    # 准备发送给浏览器的header
    response = "HTTP/1.1 200 ok\r\n"
    response += "\r\n"

    # 准备发送给浏览器的body
    f = open("./index.html", "rb")
    html_content = f.read()
    f.close()
    # response += "哈哈哈"
    new_socket.send(response.encode("utf-8"))
    new_socket.send(html_content)
    # 关闭套接字
    new_socket.close()


def main():
    """用来完成整体的控制"""
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定本地地址
    tcp_socket.bind(("", 9521))
    # 将套接字设置为监听状态
    tcp_socket.listen(128)
    while True:
        # 等待客户端的到来
        new_socket, new_adds = tcp_socket.accept()
        # 发送数据给客户端
        # 调用发送数据函数
        send_message(new_socket)
    # 关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()
