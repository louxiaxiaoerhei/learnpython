import socket

if __name__ == '__main__':
    # 创建tcp客户端套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 和服务端程序建立连接
    tcp_client_socket.connect(("192.168.160.163", 8989))

    # 接收用户下载文件的名字
    file_name = input("请输入您要下载的文件名:")

    # 对字符串进行编码转成二进制
    file_name_data = file_name.encode("gbk")
    # 发送下载文件的请求信息
    tcp_client_socket.send(file_name_data)
    #　open(file_name, "wb") 表达意思是：如果文件下载成功，再次打开文件如果是wb模式会先把文件清空然后再写入数据
    with open("/home/python/Desktop/" + file_name, "wb") as file:
        # 循环接收数据，因为服务端是循环发送的文件二进制数据的
        while True:
            file_data = tcp_client_socket.recv(1024)
            if file_data:
                # 把数据写入到指定文件
                # 多次写入数据不会清空前面的数据
                file.write(file_data)
            else:
                # 表示接收文件二进制数据成功
                break

    # 关闭套接字
    tcp_client_socket.close()