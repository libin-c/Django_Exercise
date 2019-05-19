import re
from pymysql import connect
import urllib.parse
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
def index(ret):
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

    html_template = """
                <tr>
                    <td>%d</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>
                        <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
                    </td>
                    </tr>"""

    html = ""

    for info in stock_infos:
        html += html_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[1])

    content = re.sub(r"\{%content%\}", html, content)

    return content
@route("/center.html")
def center(ret):
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
                          <td><a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a></td>
                          <td><input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s"></td></tr>
                    </tr>
                '''
    html = ""
    for line_info in stock_infos:
        html += (tr_template) % (line_info[0],line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6],line_info[0],line_info[0])

    content = re.sub(r"\{%content%\}", str(html), content)

    return content
#给路由添加正则表达式的原因：在实际开发时，url中往往会带有很多参数,例如/add/000007.html中的000007就是参数，
#如果没有正则的话，那么就需要编写N次@route来进行添加url对应的函数到字典中，此时字典中的键值对有N个，浪费空间
#而采用了正则的话，那么只需要编写一次@route就可以完成多个 url例如/add/00007.html /add/00036.html等对应同一个函数
#此时字典中键值对个数会少很多

@route(r"/add/(\d+)\.html")
def add_focus(ret):
    #1.获取股票代码
    stock_code = ret.group(1)

    #2.判断以下是否有这个股票代码
    conn = connect(host='localhost', port=3306, user='root', password='sa', database='stock_db', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()
    #sql注入功能
    sql = "select * from info where code =%s; "
    cs.execute(sql,(stock_code,))
    #如果要是没有这个股票代码，那么就认为时非法的请求
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "没有这只股票，手下留情"
    #3.判断以下是否关注过该股票
    sql = "select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"
    cs.execute(sql,stock_code)
    if cs.fetchone():
        cs.close()
        conn.close()
        return "已经关注过了，请勿重复关注"

    #4.添加关注
    sql = "insert into focus (info_id) select id from info where code=%s;"
    cs.execute(sql,stock_code)
    conn.commit()
    cs.close()
    conn.close()

    return "关注(%s)成功 " % stock_code

@route(r"/del/(\d+)\.html")
def del_focus(ret):
    #1.获取股票代码
    stock_code = ret.group(1)

    #2.判断以下是否有这个股票代码
    conn = connect(host='localhost', port=3306, user='root', password='sa', database='stock_db', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()
    #sql注入功能
    sql = "select * from info where code =%s; "
    cs.execute(sql,(stock_code,))
    #如果要是没有这个股票代码，那么就认为时非法的请求
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "没有这只股票，手下留情"
    #3.判断以下是否关注过该股票
    sql = "select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"
    cs.execute(sql,stock_code)
    #如果没有关注过表示非法的请求
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "之前未关注，请勿取消关注"

    #4.取消关注
    sql = "delete from focus where info_id = (select id from info where code=%s);"
    cs.execute(sql,(stock_code,))
    conn.commit()
    cs.close()
    conn.close()

    return "取消关注成功 "

@route(r"/update/(\d+)\.html")
def show_update_page(ret):
    '''显示修改的页面'''
    #1.获取股票代码
    stock_code = ret.group(1)

    #2.打开模板
    with open("./template/update.html", encoding='UTF-8') as f:
        content = f.read()
    # 根据股票代码查询相关的股票信息
    conn = connect(host='localhost', port=3306, user='root', password='sa', database='stock_db', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()
    sql = "select f.note_info from focus as f inner join info as i on i.id=f.info_id where i.code =%s;"
    cs.execute(sql,(stock_code,))
    stock_infos = cs.fetchone()
    note_info = stock_infos[0] #获取股票对应备注信息

    cs.close()
    conn.close()


    content = re.sub(r"\{%note_info%\}", note_info, content)
    content = re.sub(r"\{%code%\}", stock_code, content)

    return content


@route(r"/update/(\d+)/(.*)\.html")

def save_update_page(ret):
    '''保存修改的信息 '''
    stock_code = ret.group(1)
    comment = ret.group(2)
    comment = urllib.parse.unquote(comment)

    conn = connect(host='localhost', port=3306, user='root', password='sa', database='stock_db', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()
    sql ="update focus set note_info =%s where info_id =(select id from info where code = %s);"
    cs.execute(sql, (comment,stock_code))
    conn.commit()
    cs.close()
    conn.close()

    return "修改成功"









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
        for url,func in URL_FUNC_DICT.items():
            '''
            r"/index.html":index,
            r"/center.html":center,
            r"/add/\d+\.html":add_focus
            r"/del/\d+\.html":del_focus
            '''
            ret = re.match(url,file_name)
            if ret:
                return func(ret)
        else:
            return "请求的url(%s)没有对应的函数...." % file_name



    except Exception as ret:
        return "产生了异常:%s" % str(ret)
