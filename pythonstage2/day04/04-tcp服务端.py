import socket

if __name__ == '__main__':
    # 创建tcp服务端的套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口号
    tcp_server_socket.bind(("", 8989))
    # 设置监听
    # 128: 表示最大等待连接数
    # 提示： listen后的套接字由主动套接字变成被动套接字， 被动套接字表示只能接收客户端的连接请求，不能收发消息
    # 只能和客户端进行通信的是返回的那个新的套接字
    tcp_server_socket.listen(128)
    # 等待客户端的连接请求
    # 提示： 客户端和服务端连接建立成功，那么服务端就返回一个新的套接字，而新的套接字专门服务与客户端
    # 提示： 以后接收和发送数据都使用返回的新的套接字service_client_socket
    # 提示： 目前的服务端只能服务与一个客户端，后续会开发服务端可以服务于多个客户端，但是依然不能同时服务于多个客户端
    service_client_socket, ip_port = tcp_server_socket.accept()
    print(ip_port)
    # 接收客户端的数据
    # 提示： 只要一方关闭连接，那么接收一方得到的数据长度为0
    recv_data = service_client_socket.recv(1024)
    print("接收客户端的数据长度为：", len(recv_data))
    recv_content = recv_data.decode("gbk")
    print("接收客户端的数据为:", recv_content)

    # 发送数据
    service_client_socket.send("ok，问题正在处理中....".encode("gbk"))

    # 关闭连接, 表示：和客户端终止服务
    service_client_socket.close()
    # 关闭服务端套接字，表示不再提供连接请求的服务
    tcp_server_socket.close()




