from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import View

# Create your views here.


# def view_demo(request):
#     if request.method == 'GET':
#         return  HttpResponse('你用的是GET请求')
#     else:
#         return  HttpResponse('你用的是POST请求')

# 类视图
# class ViewDemo(View):
#     def get(self,request):
#         print('GET')
#         return HttpResponse('你用的是GET请求')
#     def post(self,request):
#         print('POST')
#         return HttpResponse('你用的是POST请求')
from class_view_demo.views import my_decorator


# 类视图Mixin扩展类
class MyDecoratorMixin(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        view = my_decorator(view)
        return view

class ClassViewDemo(MyDecoratorMixin,View):
    def get(self,request):
        print('GET')
        return HttpResponse('你用的是GET请求----->my_decorator_5')
    def post(self,request):
        print('POST')
        return HttpResponse('你用的是POST请求---->my_decorator_5')