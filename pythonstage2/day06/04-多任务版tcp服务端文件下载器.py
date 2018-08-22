import socket
import os
import time
import threading


# 接收客户端请求的文件名
def recv_client_request_data(service_client_socket):
    # 接收客户端请求数据
    file_name_data = service_client_socket.recv(1024)
    # 对二进制数据进行解码
    file_name = file_name_data.decode("gbk")
    print(file_name)

    # 判断请求的文件是否存在
    # 1.  os.path.exists, 2. try-except
    if os.path.exists(file_name):
        # 打开文件读取文件中的数据
        # file = open()
        # file.close()
        # with open的特点是不需要程序员自己关闭文件
        with open(file_name, "rb") as file:
            while True:
                # 读取文件中的数据
                file_data = file.read(1024)
                if file_data:
                    # 表示读取到文件中的数据了，然后把数据发送给客户端
                    service_client_socket.send(file_data)
                    time.sleep(0.5)
                else:
                    # 表示数据读取完成，跳出循环
                    print("读取文件中的数据长度:%d" % len(file_data))
                    break
    else:
        print("服务端没有找到请求的文件")

    # 终止和客户端服务
    service_client_socket.close()



if __name__ == '__main__':
    # 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口号
    tcp_server_socket.bind(("", 8989))
    # 设置监听，把主动套接字改成被动套接字，服务端的套接字只能负责接收客户端的连接请求，收发消息使用返回的新的套接字
    tcp_server_socket.listen(128)
    # 等待客户端的连接请求
    # service_client_socket: 服务于客户端的套接字
    # ip_port：客户端的ip地址和端口号
    # 提示： 如果想要服务端服务于多个客户端，那么需要让accept执行多次，因为执行一次表示接收一个客户端，多次表示可以接收多个客户端
    # 但是： 不能同时多个客户端和服务端建立连接，只能一个客户端和服务端建立连接以后，文件下载完成以后，另外一个客户端才能建立连接下载文件
    # 循环接收客户端的连接请求
    while True:

        service_client_socket, ip_port = tcp_server_socket.accept()
        print(ip_port)
        # 创建子线程
        sub_thread = threading.Thread(target=recv_client_request_data, args=(service_client_socket,))
        # 设置守护主线程
        sub_thread.setDaemon(True)
        # 启动线程执行对应的任务
        sub_thread.start()

        # # 接收客户端请求数据
        # file_name_data = service_client_socket.recv(1024)
        # # 对二进制数据进行解码
        # file_name = file_name_data.decode("gbk")
        # print(file_name)
        #
        # # 判断请求的文件是否存在
        # # 1.  os.path.exists, 2. try-except
        # if os.path.exists(file_name):
        #     # 打开文件读取文件中的数据
        #     # file = open()
        #     # file.close()
        #     # with open的特点是不需要程序员自己关闭文件
        #     with open(file_name, "rb") as file:
        #         while True:
        #             # 读取文件中的数据
        #             file_data = file.read(1024)
        #             if file_data:
        #                 # 表示读取到文件中的数据了，然后把数据发送给客户端
        #                 service_client_socket.send(file_data)
        #                 time.sleep(0.5)
        #             else:
        #                 # 表示数据读取完成，跳出循环
        #                 print("读取文件中的数据长度:%d" % len(file_data))
        #                 break
        # else:
        #     print("服务端没有找到请求的文件")
        #
        # # 终止和客户端服务
        # service_client_socket.close()
    # 关闭服务端套接字，表示不再接收客户端的连接请求
    tcp_server_socket.close()