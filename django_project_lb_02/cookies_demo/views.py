from django.shortcuts import render
from django.http.response import JsonResponse
# Create your views here.

def cookies_demo(request):
    # 接收参数
    response=JsonResponse({'key':'cookies_values'})

    # 设置cookies
    response.set_cookie('LiBin','libin@outlook.com',max_age=60)


    # 读取cookies
    ret =request.COOKIES
    print(ret)

    # 删除 cookies
    response.delete_cookie('LiBin')


    return response