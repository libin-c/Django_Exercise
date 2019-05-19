import re
from pymysql import connect
import json
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

    data = ""
    for row in stock_infos:
        data += '''<tr>
                       <td>%s</td>
                       <td>%s</td>
                       <td>%s</td>
                       <td>%s</td>
                       <td>%s</td>
                       <td>%s</td>
                       <td>%s</td>
                       <td>%s</td>
                       <td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007"></td>
                      </tr>''' % row


    content = re.sub(r"\{%content%\}",str(data),content)
    return content

@route("/center.html")
def center():
    with open("./template/center.html",encoding='UTF-8') as f:
        content = f.read()
    # my_stock_info = "这是从mysql查询出来的数据..."
    # content = re.sub(r"\{%content%\}", my_stock_info, content)
    # return content
    # 创建Connection链接
    conn = connect(host='localhost', port=3306, user='root', password='sa', database='stock_db', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()
    cs.execute("select i.code, i.short, i.chg,i.turnover, i.price, i.highs, f.note_info from info as i inner join focus as f on i.id = f.info_id;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()

    tr_template = '''
                      <tr>
                          <td>%s</td>
                          <td>%s</td>
                          <td>%s</td>
                          <td>%s</td>
                          <td>%s</td>
                          <td>%s</td>
                          <td>%s</td>
                          <td><a type="button" class="btn btn-default btn-xs" href="/update/000007.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a></td>
                          <td><input type="button" value="删除" id="toDel" name="toDel" systemidvaule="000007"></td></tr>
                    </tr>
                '''
    html = ""
    for line_info in stock_infos:
        html += (tr_template) % (line_info[0],line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6])

    content = re.sub(r"\{%content%\}", str(html), content)

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
