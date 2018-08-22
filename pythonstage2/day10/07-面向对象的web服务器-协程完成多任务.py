import socket
import re
import gevent
from gevent import monkey

# 打补丁，识别耗时操作(time.sleep, 网络请求， accept, recv)
monkey.patch_all()


# 定义Httpweb服务器类
class HttpWebServer(object):
    def __init__(self):
        # 创建tcp服务端套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置socket选项, 程序退出端口号立即释放
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口号
        tcp_server_socket.bind(("", 9090))
        # 设置监听
        tcp_server_socket.listen(128)

        # 让tcp服务器的套接字作为当前对象的属性
        self.tcp_server_socket = tcp_server_socket

    # 处理客户端请求的操作
    @staticmethod
    def handle_request_data(service_client_socket):
        # 接收客户端发送http请求报文数据, 浏览器发送get请求数据不会特别多，浏览器会进行限制，一般2k左右
        client_request_data = service_client_socket.recv(4096)
        # 对二进制数据进行解码
        client_request_content = client_request_data.decode("utf-8")
        print(client_request_content)

        # 根据正则表达式匹配请求的资源路径
        match_obj = re.search("/\S*", client_request_content)

        if match_obj:
            # 获取请求的资源路径
            request_path = match_obj.group()
            print(request_path)
            if request_path == "/":
                # 如果用户请求的根目录那么指定成首页信息
                request_path = "/index.html"

            # 1. os.path.exits("static"+request_path) 判断请求的资源路径是否存在
            # 2. try-except, 如果出现异常表示文件不存在 返回404的信息

            try:
                # 读取index.html的数据
                # rb: 这个模式可以兼容文本文件和图片文件
                with open("static" + request_path, "rb") as file:
                    # 获取文件中的全部数据
                    file_data = file.read()

            except Exception as e:
                # 出现异常返回404的信息
                # 响应行
                response_line = "HTTP/1.1 404 Not Found\r\n"
                # 响应头
                # Content-Type: text/html;charset=utf-8
                # 服务器告诉浏览器发送数据的内容类型及内容的编码格式
                # 扩展： 响应头里面的数据可以程序员自己定义
                response_header = "Server: PWS/1.1\r\nContent-Type: text/html;charset=utf-8\r\nabc:ok\r\n"
                # 响应体
                response_body = "<h1>非常抱歉，您当前访问的网页已经不存在了</h1>"
                # 准备响应报文数据
                response_data = (response_line + response_header + "\r\n" + response_body).encode("utf-8")

                # 发送http响应报文数据
                service_client_socket.send(response_data)
            else:

                # 响应行
                response_line = "HTTP/1.1 200 OK\r\n"
                # 响应头
                # Content-Type: text/html;charset=utf-8
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

    # 启动web服务器进行工作
    def start(self):
        while True:
            # 等待客户端的连接请求
            service_client_socket, ip_port = self.tcp_server_socket.accept()
            # 创建协程并执行对应的任务
            gevent.spawn(self.handle_request_data, service_client_socket)


if __name__ == '__main__':

    # 创建web服务器对象
    web_server = HttpWebServer()
    # 启动服务器进行工作
    web_server.start()





