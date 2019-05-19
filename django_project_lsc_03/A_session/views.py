# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseForbidden
from django.views import View











#会话
def session(request):
    # 通过HttpRequest对象的session属性进行会话的读写操作。

    # 1.以键值对的格式写session
    # request.session['键']=值
    request.session["name"]="xiuxiuguai"
    request.session["age"] = "man"
    request.session["school"] = "Massachusetts Institute of Technology"
    request.session["brithday"] = "1999.9.19"

    #2.根据键读取值。
    ##request.session.get('键',默认值)
    # ret = request.session.get("school","lalalallala")
    # print("School  : %s" % ret)

    #3.清除所有session，在存储中删除值部分。
    # request.session.clear()

    #4.清除session数据，在存储中删除session的整条数据。
    # request.session.flush()

    #5.删除session中的指定键及值，在存储中只删除某个键及对应的值。
    # del request.session['键']
    # del request.session["school"]

    #6.设置session的有效期
    # request.session.set_expiry(value)
    # 不写, 设置为 None 都是 14天 2周
    # 写 秒数
    # 0 会话结束
    request.session.set_expiry(60)



    return HttpResponse("session 测试啦啦啦")