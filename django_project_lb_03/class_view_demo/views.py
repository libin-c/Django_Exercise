from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import  View
from django.utils.decorators import method_decorator
# Create your views here.

# 装饰器
def my_decorator(func):

    def wrapper(request,*args,**kwargs):
        print('自定义装饰器被调用了')
        print('请求路径%s' % request.path)
        print('请求方式%s' % request.method)
        return func(request,*args,**kwargs)

    return wrapper


# # 类视图
# class ClassViewDemo(View):
#     def get(self,request):
#         print('GET')
#         return HttpResponse('你用的是GET请求')
#     def post(self,request):
#         print('POST')
#         return HttpResponse('你用的是POST请求')

# # 类视图 调用装饰器__01
# class ClassViewDemo(View):
#     def get(self,request):
#         print('GET')
#         return HttpResponse('你用的是GET请求----->my_decorator')
#     def post(self,request):
#         print('POST')
#         return HttpResponse('你用的是POST请求---->my_decorator')

# 类视图 调用装饰器__02 @method_decorator(my_decorator,name='get')   缺点 想给哪个加必须name='8大请求方式'
# @method_decorator(my_decorator,name='get')


# #类视图 调用装饰器__03 @method_decorator(my_decorator,name='dispatch')
# @method_decorator(my_decorator,name='dispatch')
# class ClassViewDemo(View):
#     def get(self,request):
#         print('GET')
#         return HttpResponse('你用的是GET请求----->my_decorator_2')
#     def post(self,request):
#         print('POST')
#         return HttpResponse('你用的是POST请求---->my_decorator_2')

#类视图 调用装饰器__03 @method_decorator(my_decorator,name='dispatch')
@method_decorator(my_decorator,name='dispatch')
class ClassViewDemo(View):
    def get(self,request):
        print('GET')
        return HttpResponse('你用的是GET请求----->my_decorator_3')
    def post(self,request):
        print('POST')
        return HttpResponse('你用的是POST请求---->my_decorator_3')

# #类视图 调用装饰器__04 给每个函数都加@method_decorator(my_decorator)   @method_decorator作用把每个类方法实例对象变成函数 去掉self 参数 导致第一个参数是request参数
# @method_decorator(my_decorator,name='dispatch')
# class ClassViewDemo(View):
#     @method_decorator(my_decorator)
#     def get(self,request):
#         print('GET')
#         return HttpResponse('你用的是GET请求----->my_decorator_4')
#
#     @method_decorator(my_decorator)
#     def post(self,request):
#         print('POST')
#         return HttpResponse('你用的是POST请求---->my_decorator_4')