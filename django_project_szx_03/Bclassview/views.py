from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseForbidden
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.
# Create your views here.



# 扩展类Mixin
class RegisterMixin(object):
    def put(self,request,**kwargs):
        print('PUT的方法！！！')
        return HttpResponse('这是扩展类!!')

class CaptchaMixin(object):
    def put(self,request,**kwargs):
        print('delete！！！')
        return HttpResponse('这是delete扩展类!!')

class rubbishView(RegisterMixin,CaptchaMixin,View):
    def get(self, request):
        return HttpResponse('--皇家澳门赌场首页(李舜丞教我的)--')

    def post(self, request):
        return HttpResponse('--性感老张在线喝水--')
#

#  装饰器
def the_decorator(func):
    def zhuangshi(request,**kwargs):
        print('装饰器添加成功！！！！！！',request.method)
        return func(request,**kwargs)
    return zhuangshi




@method_decorator(the_decorator,name='dispatch')
# 类视图-----易扩展，自动判断，阅读性高
class rubbishView(View):
    def get(self,request):
        return HttpResponse('--皇家澳门赌场首页(李舜丞教我的)--')

    def post(self, request):
        return HttpResponse('--性感老张在线喝水--')



# 定义一个视图函数  手动判断还特么的想多功能
def index(request):
    """处理注册"""

    # 获取请求方法，判断是GET/POST请求
    if request.method == 'GET':

        return HttpResponse('澳门赌场首页')
    else:

        return HttpResponse('欢迎来到德莱联盟')