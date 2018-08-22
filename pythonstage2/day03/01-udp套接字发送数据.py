import socket

# 判断是否是程序的入口，或者判断是否是主模块
# 提示： 直接运行的模块就是主模块
if __name__ == '__main__':
    # 1. AF_INET: ip地址类型，表示ipv4, AF_INET6表示ipv6
    # 2. SOCK_DGRAM:表示udp传输协议的类型（udp， tcp）
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 准备数据
    send_content = "哈哈，今天学习了socket!"
    # 对字符串进行编码转成二进制数据
    # window的网络调试助手使用gbk
    # 乌班图的网络调试助手使用utf-8
    send_data = send_content.encode("gbk")
    # 发送数据
    # 1. 发送的数据
    # 2. 元组类型: 表示对方的ip地址和对方的端口号
    udp_socket.sendto(send_data, ("192.168.152.177", 9090))
    # 关闭套接字
    udp_socket.close()