from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseForbidden
# Create your views here.
def indexSession(request):
    request.session['itcast'] = 'Oooops'
    request.session['lsc'] = 'cxk'
    request.session['zhang'] = 'rubbish'
    # 设置时间的  射了150秒
    request.session.set_expiry(150)
    # ret = request.session.get("itcast")
    # 清除session
    # del request.session['itcast']
    # 全特么删了
    # request.session.clear()
    # 删除整条
    request.session.flush()




    return HttpResponse('我他妈的操作session')