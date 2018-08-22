import socket
import threading


# 收发客户端消息函数
def recv_client_data(service_client_socket, ip_port):
    # 循环接收客户端发送的消息
    while True:
        # 接收客户端的消息
        recv_data = service_client_socket.recv(1024)
        if recv_data:
            # 解码数据
            recv_content = recv_data.decode("gbk")
            print("接收的数据为:", recv_content, ip_port)
            # 给客户端发送数据
            service_client_socket.send("ok...".encode("gbk"))
        else:
            print(ip_port, "客户端下线了")
            break

    # 终止和客户端服务
    service_client_socket.close()



if __name__ == '__main__':
    # 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 程序退出端口号立即释放
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口号
    tcp_server_socket.bind(("", 9090))
    # 设置监听
    tcp_server_socket.listen(128)
    # 循环接收客户端的连接请求，相当于可以接收多个客户端
    while True:
        # 等待接收客户端的连接请求
        service_client_socket, ip_port = tcp_server_socket.accept()
        print("客户端连接成功:", ip_port)

        # 创建子线程
        recv_thread = threading.Thread(target=recv_client_data, args=(service_client_socket, ip_port), daemon=True)
        # 启动线程执行对应的任务
        recv_thread.start()



        # # 循环接收客户端发送的消息
        # while True:
        #     # 接收客户端的消息
        #     recv_data = service_client_socket.recv(1024)
        #     if recv_data:
        #         # 解码数据
        #         recv_content = recv_data.decode("gbk")
        #         print("接收的数据为:", recv_content, ip_port)
        #         # 给客户端发送数据
        #         service_client_socket.send("ok...".encode("gbk"))
        #     else:
        #         print(ip_port, "客户端下线了")
        #         break
        #
        # # 终止和客户端服务
        # service_client_socket.close()
    # 关闭服务端套接字, 提示： 服务端的套接字可以不用关，因为服务端需要一直运行
    tcp_server_socket.close()