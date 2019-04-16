import socket
import threading
import re
import multiprocessing
import gevent
from gevent import monkey

monkey.patch_all()


def server_client(new_server_socket):
    """为客户端返回数据"""
    # 接收浏览器发送过来的请求，即http请求
    # GET /index.html HTTP/1.1
    # ...
    request = new_server_socket.recv(1024).decode("utf-8")
    request_lines = request.splitlines()
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    file_name = ""
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"

    try:
        f = open("./html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "----file not found----"
        new_server_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        response = "HTTP/1.1 200 ok\r\n"
        response += "\r\n"
        new_server_socket.send(response.encode("utf-8"))
        new_server_socket.send(html_content)
    new_server_socket.close()


def main():
    """主函数实现整体的控制"""
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 下面这行代码实现：如果服务器先调用close段时间内服务器仍然可以使用同一个端口
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定本地地址
    tcp_server_socket.bind(("", 9527))
    # 设置为监听状态
    tcp_server_socket.listen(128)
    while True:
        # 接收客户端的到来
        new_server_socket, new_server_addr = tcp_server_socket.accept()
        # 为客户端发送数据
        # 创建线程
        # p = threading.Thread(target=server_client, args=(new_server_socket,))
        # 创建进程
        # p = multiprocessing.Process(target=server_client, args=(new_server_socket,))
        # p.start()
        # 创建协程
        gevent.spawn(server_client, new_server_socket)
        new_server_socket.close()  # 当使用进程时需要这行代码来关闭新的套接字，因为进程不共享全局变量
        # 当使用线程和协程时不需要这行代码，因为他们共享全局变量，
        # 在server_client()函数中new_server_socket已经关闭
    # 关闭套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
