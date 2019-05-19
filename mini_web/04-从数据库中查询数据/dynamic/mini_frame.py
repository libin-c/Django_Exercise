import re
from pymysql import connect
'''
URL_FUNC_DICT = {
    "/index.html":index,
    "/center.html":center
}
'''
URL_FUNC_DICT = dict()

# func_list = list() 理解字典过程结合最下面 func_list.append(func)
def route(url):
    def set_func(func):
        #func_list.append(func)#装所有被装饰器装饰过的引用
        #URL_FUNC_DICT["/index.py"] = index
        URL_FUNC_DICT[url] = func
        def call_func(*args,**kwargs):
            return func(*args,**kwargs)
        return call_func
    return set_func

@route("/index.html")
def index():
    with open("./template/index.html",encoding='UTF-8') as f:
        content= f.read()
    # my_stock_info = "哈哈哈哈，这是你的本月名称....."

    #创建Connection链接
    conn = connect(host = 'localhost',port=3306,user='root',password='sa',database='stock_db',charset='utf8')
    #获得Cursor对象
    cs = conn.cursor()
    cs.execute("select * from info;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()
    content = re.sub(r"\{%content%\}",str(stock_infos),content)




    return content

@route("/center.html")
def center():
    with open("./template/center.html",encoding='UTF-8') as f:
        content = f.read()
    my_stock_info = "这是从mysql查询出来的数据..."
    content = re.sub(r"\{%content%\}", my_stock_info, content)
    return content



def application(env,start_response):
    start_response("200 OK",[("Content-Type","text/html;charset=utf-8")])

    file_name = env['PATH_INFO']
    #file_name = "/index.py"

    # if file_name =="/index.py":
    #     return index()
    # elif file_name == "/center.py":
    #     return center()
    # else:
    #     return "welcome to 嗅嗅怪的low逼框架"
    #取value
    # func = URL_FUNC_DICT[file_name]
    #     # return func()
    #采用异常try 而不采用 if "name" in URL_FUNC_DICT,异常有传递性
    try:
        return URL_FUNC_DICT[file_name]()
    except Exception as ret:
        return "产生了异常:%s" % str(ret)
