from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import View
import time
# Create your views here.

def session_demo(request):

    # # 1.0 设置session
    request.session['LiBin']='libin@outlook.com'
    request.session['year'] = 2019
    request.session['555'] = 777
    request.session['666'] = 888
    #
    # # 2.0 设置 session的过期时间
    # request.session.set_expiry(None)

    # 3.0  获取session的值
    ret = request.session.get('LiBin')

    # 4.0 删除 指定键
    del request.session['LiBin']
    #
    # # 4.1 删除所有session 键值
    request.session.clear()
    #
    # # 4.2 删除 所有session
    request.session.flush()

    return HttpResponse('设置session 内容为:%s'%ret)

class TemplatesDemo(View):
    def get(self,request):
        context = {
            'message':time.ctime()
        }
        return render(request,'index.html',context=context)