import socket

if __name__ == '__main__':
    # 创建tcp客户端套接字
    # 1. AF_INET： ipv4地址类型
    # 2. SOCK_STREAM: 表示使用的tcp传输协议的类型
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 和服务端程序建立连接
    tcp_client_socket.connect(("192.168.160.163", 9876))
    # 代码执行到此，说明建立连接成功
    send_content = "哈哈，我是客户端小白!"
    # 对字符串进行编码
    send_data = send_content.encode("gbk")
    # 发送数据
    tcp_client_socket.send(send_data)
    # 接收数据,接收一次数据，这个数据最大是1024个字节
    recv_data = tcp_client_socket.recv(1024)
    # 对二进制数据进行解码
    recv_content = recv_data.decode("gbk")
    print("接收服务端的数据为:", recv_content)
    # 关闭连接
    tcp_client_socket.close()