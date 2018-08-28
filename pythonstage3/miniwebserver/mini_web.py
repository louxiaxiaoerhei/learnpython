import socket
import gevent
import re
import os
from gevent import monkey
monkey.patch_all()


class WebServer(object):
    def __init__(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        server_socket.bind(("", 8080))
        server_socket.listen(128)
        self.server_socket = server_socket

    @staticmethod
    def handle_request(server_client_socket):
        client_request_data = server_client_socket.recv(4096)
        request_content = client_request_data.decode()
        match_obj = re.search("/\S*", request_content)
        if match_obj:
            request_path = match_obj.group()
            if request_path == "/":
                request_path = "/index.html"
            request_file_path = "./static" + request_path
            print(request_file_path)
            try:
                with open(request_file_path, "rb") as file:
                    response_file_data = file.read()
            except Exception as e:
                # print(e+"文件找不到....")
                response_line = "HTTP/1.1 404 Not Fount\r\n"
                response_header = "Server: PWS/1.1\r\nContent-Type: text/html;charset=utf-8\r\nabc:ok\r\n"
                response_body = "<h1>非常抱歉，您当前访问的网页已经不存在了</h1>"
                response_data = (response_line + response_header + "\r\n" + response_body).encode("utf-8")
                server_client_socket.send(response_data)
            else:
                response_line = "HTTP/1.1 200 OK\r\n"
                response_header = "Server: PWS/1.1\r\n"
                response_body = response_file_data
                response_data = (response_line + response_header + "\r\n").encode() + response_body
                server_client_socket.send(response_data)
            finally:
                server_client_socket.close()

    def start(self):
        print("服务器启动......")
        while True:
            server_client_socket, ip_port = self.server_socket.accept()
            print(ip_port, "链接成功...")
            gevent.spawn(self.handle_request, server_client_socket)


def main():
    web_server = WebServer()
    web_server.start()


if __name__ == '__main__':
    main()
