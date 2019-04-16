import socket

tcp_server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_tcp.bind("", 9527)
tcp_server_tcp.listen(128)
tcp_server_tcp.setblocking(False)  # 设置套接字为非堵塞的方式
client_socket_list = list()

while True:
    try:
        new_socket, new_addr = tcp_server_tcp.accept()
    except Exception as ret:
        print("没有新客户端的到来")
    else:
        print("---只要没有产生异常那麽就意味着来了一个新的客户端---")
        new_socket.setblocking(False)  # 设置套接字为非堵塞的方式
        client_socket_list.append(new_socket)
    for client_socket in client_socket_list:
        try:
            recv_data = client_socket.recv(1024)
        except Exception as ret:
            print(ret)
            print("---这个客户端没有发送过来数据---")
        else:
            print("---没有异常---")
            print(recv_data)
            if recv_data:
                print("客户端发送过来了数据")
            else:
                # 对方调用了close函数导致了recv返回
                client_socket.close()
                client_socket_list.remove(client_socket)
                print("---客户端已经关闭---")
