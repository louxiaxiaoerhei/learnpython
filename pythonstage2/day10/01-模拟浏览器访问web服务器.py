import socket

if __name__ == '__main__':
    # 创建tcp客户端的套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 和服务器的web应用程序建立连接
    tcp_client_socket.connect(("tlias3.boxuegu.com", 80))

    # 请求行
    request_line = "GET / HTTP/1.1\r\n"
    # 请求头
    # request_header = "Host: tlias3.boxuegu.com\r\nConnection: close\r\n"

    request_header = "Host: tlias3.boxuegu.com\r\n"

    # 准备http请求报文数据
    request_content = request_line + request_header + "\r\n"

    # 对字符串进行编码
    request_data = request_content.encode("utf-8")

    # 发送http请求报文数据
    tcp_client_socket.send(request_data)

    # 定义二进制数据类型
    result = b''
    while True:
        # 接收http响应报文数据
        recv_data = tcp_client_socket.recv(1024)

        # 扩展：--
        # 判断服务端发送的数据长度，Content-Length:100
        # 判断服务器发送的数据长度，Transfer-Encoding， 判断是否有结束标记: \r\n0\r\n
        if recv_data:
            # 拼接每次获取的二进制数据
            result += recv_data
            # print(recv_data)
            # if len(result) >= 100:
            #     break
            # 判断是否有接收标记，找到了就不再等着获取服务端的数据了
            if result.rfind(b'\r\n0\r\n') != -1:
                break
        else:
            break

    print(result)
    # 根据二进制数据标示符分割数据，只分割1次
    response_list = result.split(b'\r\n\r\n', maxsplit=1)
    print(len(response_list))
    print(response_list[1])

    # 获取响应体的数据并对其进行解码
    response_body = response_list[1].decode("utf-8")
    print(response_body)
    tcp_client_socket.close()