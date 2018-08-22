import socket

if __name__ == '__main__':
    # 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置socket选项, 程序退出端口号立即释放
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口号
    tcp_server_socket.bind(("", 9090))
    # 设置监听
    tcp_server_socket.listen(128)
    while True:
        # 等待客户端的连接请求
        service_client_socket, ip_port = tcp_server_socket.accept()

        # 接收客户端发送http请求报文数据, 浏览器发送get请求数据不会特别多，浏览器会进行限制，一般2k左右
        client_request_data = service_client_socket.recv(4096)
        print(client_request_data)

        # 读取index.html的数据
        # rb: 这个模式可以兼容文本文件和图片文件
        with open("index.html", "rb") as file:
            # 获取文件中的全部数据
            file_data = file.read()

        # 响应行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 响应头
        #Content-Type: text/html;charset=utf-8
        # 服务器告诉浏览器发送数据的内容类型及内容的编码格式
        # 扩展： 响应头里面的数据可以程序员自己定义
        response_header = "Server: PWS/1.1\r\nContent-Type: text/html;charset=utf-8\r\nabc:ok\r\n"
        # 响应体
        response_body = file_data
        # 准备响应报文数据
        response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body

        # 发送http响应报文数据
        service_client_socket.send(response_data)
        service_client_socket.close()


