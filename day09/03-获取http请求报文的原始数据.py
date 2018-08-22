import socket

if __name__ == '__main__':
    # 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口号
    tcp_server_socket.bind(("", 9090))
    # 设置监听
    tcp_server_socket.listen(128)
    # 等待接收客户端的连接请求
    service_client_socket, ip_port = tcp_server_socket.accept()
    print(ip_port)
    # 接收客户端发送给服务端的http请求报文的数据
    recv_data = service_client_socket.recv(4096)

    print(recv_data)
    service_client_socket.close()
    tcp_server_socket.close()