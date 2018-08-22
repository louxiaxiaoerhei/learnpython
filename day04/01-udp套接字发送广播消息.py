import socket

# 判断是否是程序的入口
if __name__ == '__main__':
    # 创建udp的套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 设置socket选项，开启广播功能选项
    # 1. SOL_SOCKET: 表示当前socket
    # 2. SO_BROADCAST： 表示广播选项
    # 3. True： 开启广播选项
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
    # 发送广播消息
    # udp_socket.sendto("大家好，我是大家的授课老师，多多关照!".encode("gbk"), ("192.168.160.255", 9090))
    # ctr + d: 复制当前行
    udp_socket.sendto("大家好，我是大家的授课老师，多多关照!".encode("gbk"), ("255.255.255.255", 9090))

    # 192.168.160.255  表示160网段的广播地址
    # 255.255.255.255  表示通用的广播地址

    # 关闭套接字
    udp_socket.close()