import socket

if __name__ == '__main__':
    # 创建udp的套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 发送数据
    udp_socket.sendto("哈哈，这次又来测试啦~".encode("gbk"), ("192.168.152.178", 9091))
    # 接收数据
    # 1024: 表示每次接收数据的最大字节数
    recv_data, dst_ip_port = udp_socket.recvfrom(1024)
    print(recv_data, dst_ip_port)

    # 对二进制数据进行解码得到字符串
    recv_content = recv_data.decode("gbk")
    print(recv_content, dst_ip_port)

    # 关闭套接字
    udp_socket.close()