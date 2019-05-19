def index():
    with open("./template/index.html") as f:
        return f.read()


def center():
    with open("./template/center.html") as f:
        return f.read()



def application(env,start_response):
    start_response("200 OK",[("Content-Type","text/html;charset=utf-8")])

    file_name = env['PATH_INFO']
    #file_name = "/index.py"

    if file_name =="/index.py":
        return index()
    elif file_name == "/center.py":
        return center()
    else:
        return "welcome to 嗅嗅怪的low逼框架"

