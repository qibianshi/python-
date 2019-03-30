import socket


def main():
    """tcp通信服务器"""
    # 1.买个手机（创建套接字 socket）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.插入电话卡（绑定本地信息 bind）
    tcp_server_socket.bind(("192.168.23.131", 9527))
    # 3.将手机设置为正常的响铃模式（让默认的套接字由主动变为被动 即监听状态 listen）
    tcp_server_socket.listen(128)
    while True:
        print("等待一个新的客户端的到来...")
        # 4.等待别人的电话到来（等待客户端的链接 accept）
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("一个新的客户端已经到来：%s" % client_addr)
        while True:
            # 5.接收客户端发送过来的请求
            recv_data = new_client_socket.recv(1024)
            print("客户端发送过来的请求是：%s" % recv_data.encode("utf-8"))
            # 如果recv解堵塞，那麽有2种方式
            # 1.recv接收到客户端发送过来的数据
            # 2.客户端调用close导致了这里的recv解堵塞
            if recv_data:
                # 6.回送一部分数据给客户端
                new_client_socket.send("hahahah".encode("gbk"))
            else:
                break
        # 7.关闭套接字
        new_client_socket.close()
        print("本次服务结束！")
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
