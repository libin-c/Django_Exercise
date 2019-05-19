from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render
# 类视图--易扩展, 自动判断 ,阅读性高
from django.views import View
# method_decorator 将 类里面函数 转换出来
from django.utils.decorators import method_decorator

#装饰器1号  给父类 RegisterMixin 中的所有方法装饰
def my_decorator_1(func):
    def fakerMixin(request,**kwargs):
        #扩展的内容
        print("lielielielielielie SKT输啦哟哟哟",request.method)
        return func(request, **kwargs)
    return fakerMixin

#装饰器2号  给父类 LogoutMixin 中的所有方法装饰
def my_decorator_2(func):
    def philosopher(request,**kwargs):
        print("在我的BGM没人可以骚得过我",request.method)
        return func(request, **kwargs)
    return philosopher


#多继承
class RegisterMixin(object):
    #首先调用类方法
    @classmethod
    def as_view(cls,*args,**kwargs):
        view =super().as_view(*args,**kwargs)
        view = my_decorator_1(view)#灵魂代码
        return view

    #     #dispatch中的8种请求方式
    def get(self,request,*args,**kwargs):
        return HttpResponse("这是get请求,请求的url会附带查询参数---查询参数在QueryString保存")

class LogoutMixin(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        view = my_decorator_2(view)
        return view

        # dispatch中的8种请求方式
    def post(self,request,*args,**kwargs):
        return HttpResponse("这是post请求,请求的url不带参数---查询参数在WebForms保存")



class LoginMixin(RegisterMixin,LogoutMixin,View):
    def put(self,request,*args,**kwargs):
        return HttpResponse("用于向指定URL传送更新资源，是幂等的。 比如修改用户密码，")
















#装饰器0号
def my_decorator(func):
    def inner_func(request,**kwargs):
        print("增加了新功能哈哈哈",request.method)
        return func(request,**kwargs)
    return inner_func

#类视图自动调用
# 1.1 只能给其中一个函数 添加
# @method_decorator(my_decorator, name="post")
# 1.2 给所有函数
@method_decorator(my_decorator, name="dispatch")
class AutomaticTest(View):
    def get(self,request):
        return HttpResponse("@@@@@自动校验----->get")

    def post(self,request):
        a = request.POST.get('a')
        print(a)
        return HttpResponse("#####自动校验----->post")



#视图函数手动调用
def handTest(request):
    if request.method=="get":
        return HttpResponse("手动校验----->get")
    else:
        return HttpResponse("手动校验----->post")
