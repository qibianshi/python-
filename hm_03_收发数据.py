import socket


def send_message(udp_socket):
    dest_ip = input("请输入对方的ip地址：")
    dest_port = int(input("请输入对方的端口号："))
    while True:
        send_data = input("请输入要发送的数据：")
        print("返回上一级请按[b]")

        if send_data == "b":
            break
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def receive_message(udp_socket):
    # 绑定本地地址信息
    udp_socket.bind(("", 9527))
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_data[1]), recv_data[0].decode("gbk")))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 9527))
    while True:
        print("发送数据：[1]")
        print("接收数据：[2]")
        print("退出程序：[0]")
        input_str = input("请输入您要进行的操作：")
        if input_str == "1":
            # 发送数据
            send_message(udp_socket)
        elif input_str == "2":
            # 接受数据
            receive_message(udp_socket)

        elif input_str == "0":
            print("退出程序！")
            break
        else:
            print("您输入的操作有误，请重新输入！")

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
