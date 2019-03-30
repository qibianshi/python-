import socket

def main():
    #  创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 可以使用套接字收发数据
    # udp_socket.sendto("hello anpengyu", 对方的ip以及port)
    udp_socket.sendto(b"hello anpengyu", ("192.168.23.1", 8080))
    # 关闭套接字
    udp_socket.close()
    print("------run------")
if __name__ == "__main__":
    main()
