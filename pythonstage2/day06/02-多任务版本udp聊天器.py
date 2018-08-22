import socket
import threading


# 发送数据
def send_msg(current_socket):
    # 接收用户输入的数据
    send_content = input("请输入您要发送的内容:")
    # 对字符串进行gbk编码转成二进制
    send_data = send_content.encode("gbk")
    # 发送数据
    current_socket.sendto(send_data, ("192.168.160.149", 9898))


# 接收数据
def recv_msg(current_socket):
    # 循环接收对方发送的消息
    while True:
        recv_data, ip_port = current_socket.recvfrom(1024)
        # 对二进制数据使用gbk解码
        recv_content = recv_data.decode("gbk")
        print("接收的到的数据为:", recv_content, ip_port, sep="&&")


if __name__ == '__main__':
    # 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定端口号
    udp_socket.bind(("", 9090))

    # 创建接收数据的线程
    recv_thread = threading.Thread(target=recv_msg, args=(udp_socket,))
    # 设置守护主线程
    recv_thread.setDaemon(True)
    recv_thread.start()

    while True:
        # 接收用户的功能选项
        menu_option = input("请输入功能选项 0.退出 1.发送")
        if menu_option == "1":
            # 发送数据
            send_msg(udp_socket)
        elif menu_option == "0":
            break

    # 关闭套接字
    udp_socket.close()
