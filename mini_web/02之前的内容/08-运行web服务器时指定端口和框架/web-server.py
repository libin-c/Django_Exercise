import socket
import re
import multiprocessing
import dynamic.mini_frame
import sys


class WSGIServer(object):
    def __init__(self,port):
        # 1.创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # TCP三次握手四次挥手 服务器资源保存2-4min 这句话，如果服务器先挂了，不会出问题
        # 2.绑定
        self.tcp_server_socket.bind(("", port))
        # 3.变为监听套接字
        self.tcp_server_socket.listen(128)

    def service_client(self, new_socket):
        # 1.接收浏览器发送过来的请求，即http请求
        # GET /HTTP/1.1
        # ...
        request = new_socket.recv(1024).decode("utf-8")
        # print(">>>"*50)
        # print(request)
        request_lines = request.splitlines()
        print(" ")
        print(">" * 20)
        print(request_lines)

        # GET /index.html HTTP/1.1
        # get post put del
        file_name = ""
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        if ret:
            file_name = ret.group(1)
            # print("-"*50,file_name)
            if file_name == "/":
                file_name = "/index.html"

        # 2.返回http格式的的数据，给浏览器
        # 2.1如果请求的资源不是以.py结尾，那么就认为是静态资源（html/css/js/png）
        if not file_name.endswith(".py"):
            try:
                f = open("./static" + file_name, "rb")
            except:
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "--------------file not found-----------"
                new_socket.send(response.encode("utf-8"))

            else:
                html_content = f.read()
                f.close()
                # 2.1准备发送给浏览器的数据---header
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                # 2.2将response header发送给浏览器
                new_socket.send(response.encode("utf-8"))
                # 将response body 发送给浏览器
                new_socket.send(html_content)
        else:
            # 2.2如果以.py结尾，那么就认为是动态资源请求
            env = dict()
            #判断注册登录各种
            env['PATH_INFO'] = file_name

            body = dynamic.mini_frame.application(env, self.set_response_header)

            header = "HTTP/1.1 %s\r\n"%self.status

            for temp in self.headers:
                header += "%s:%s\r\n"%(temp[0],temp[1])

            header += "\r\n"

            # if file_name =="/login.py":
            #     body = mini_frame.login()
            # elif file_name =="/register.py":
            #     body = mini_frame.register()
            response = header + body
            # 发送response给浏览器

            new_socket.send(response.encode("utf-8"))

        # 关闭套接字
        new_socket.close()

    def set_response_header(self,status,headers):
        self.status = status
        # self.headers = headers
        self.headers = [("server","miniweb V9.6")]#服务器信息
        self.headers += headers#框架信息

    def run_forever(self):
        '''用来完成整体的控制'''

        while True:
            # 4.等待新客户端链接
            new_socket, client_adrr = self.tcp_server_socket.accept()
            # 5.为这个客户端服务
            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            # 通过元祖方式把新的套接字new_socket 扔去指定的进程中
            p.start()
            new_socket.close()
        # 关闭监听套接字
        self.tcp_server_socket.close()


def main():
    # 控制整体创建服务器对象，然后调用这个对象的run_forever方法
    if len(sys.argv) ==2:
        try:
            port = int(sys.argv[1])
        except Exception as ret:
            print("端口输入错误～～～～")
            return
    else:
        print("请按照以下方式运行:")
        print("python3 xxx.py 7890")
        return

    wsgi_server = WSGIServer(port)
    wsgi_server.run_forever()


if __name__ == '__main__':
    main()