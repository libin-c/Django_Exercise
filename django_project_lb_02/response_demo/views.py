from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.response import JsonResponse
# Create your views here.
def response_demo(request):
    #   参数



    # return HttpResponse(
    #     # 响应体
    #     content="content 参数 响应体",
    #     # MIME 文件交互格式
    #     content_type='text/html ; charset=utf-8',
    #     # 状态码
    #     status=200
    #
    # )





    # #对象属性
    # response = HttpResponse()
    # response.content='content 类对象  响应体'
    # response.status_code=202
    # response['LiBin']='libin@outlook.com'
    # return response


    # JsonResponse 子类
    # JsonResponse 帮我们做两件事
    # 01. 帮我们讲数据转换为json
    # 02. 将content_type 转换成 application/json

    # dict_data = '''{
    #     "name":"小美眉",
    #     "gender":False,
    #     "age":18
    # }'''
    # return  HttpResponse(dict_data)
    # HttpResponse 默认接收字符串

    # json 字典
    # dict_data = {
    #     "name":"小美眉",
    #     "gender":False,
    #     "age":18
    # }
    # return JsonResponse(dict_data)

    # 列表 需要加 safe=False
    list_data=[
        {
        "name":"小美眉",
        "gender":False,
        "age":18
        },
        {
            "name": "小美眉",
            "gender": False,
            "age": 18
        },
        {
            "name": "小美眉",
            "gender": False,
            "age": 18
        },

    ]
    return JsonResponse(list_data,safe=False)
