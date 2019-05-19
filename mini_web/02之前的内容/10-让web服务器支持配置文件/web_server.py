import socket
import re
import multiprocessing
# import dynamic.mini_frame
import sys


class WSGIServer(object):
    def __init__(self,port,app,static_path):
        # 1.创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # TCP三次握手四次挥手 服务器资源保存2-4min 这句话，如果服务器先挂了，不会出问题
        # 2.绑定
        self.tcp_server_socket.bind(("", port))
        # 3.变为监听套接字
        self.tcp_server_socket.listen(128)

        self.application = app
        self.static_path = static_path

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
                f = open(self.static_path + file_name, "rb")
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

            body = self.application(env, self.set_response_header)

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
        self.headers = [("server","mini_web V9.6")]#服务器信息
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
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[1])
            frame_app_name = sys.argv[2]
        except Exception as ret:
            print("端口输入错误～～～～")
            return
    else:
        print("请按照以下方式运行:")
        print("python3 xxx.py 7890 mini_frame:application")
        return

    #mini_frame:application
    ret = re.match(r"([^:]+):(.*)", frame_app_name)
    if ret:
        frame_name = ret.group(1)  # mini_frame
        app_name = ret.group(2)  # application
    else:
        print("请按照以下方式运行:")
        print("python3 xxx.py 7890 mini_frame:application")
        return

    with open("./web_server.conf") as f:
        conf_info = eval(f.read())
        #此时conf_info是一个字典，数据为
    '''
    {
	"static_path":"./static",
	"dynamic_path":"./dynamic"
    }
    '''


    sys.path.append(conf_info["dynamic_path"])#找到mini_frame的路径

    # import frame_name   找不到的 因为import将frame_name当成模块名，而不是变量去解析
    #找frame_name.py
    frame = __import__(frame_name)#返回值是一个对象 标记导入的这个模块
    app = getattr(frame,app_name)#此时 app 就指向了 dynamic/mini_frame模块中的application这个函数

    wsgi_server = WSGIServer(port,app,conf_info["static_path"])
    wsgi_server.run_forever()


if __name__ == '__main__':
    main()