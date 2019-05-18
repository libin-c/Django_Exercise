from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

#1.URL路径请求
# def weather(request,city,year):
#     print("year")
#     print("city")
#     return HttpResponse("year : %s,city: %s" %(year,city))

#2.查询子字符串
#  /qs/?a=1&b=2&a=3
# def qs(request):
#     #GET是属性不是请求方法    无论是post或者是GET 都可以通过request.GET获取请求中的查询字符串数据。
#     params = request.GET
#     print(params)
#     a = params.get('a')#字典键不重复
#     b = params.get('b')
#     alist = params.getlist('a') #取出a的所有值
#
#     print(a)  # 3
#     print(b)  # 2
#     print(alist)  # ['1', '3']
#     return HttpResponse('查询子字符串')

#3.1请求体参数 body 表单类型
# 可以发送请求体数据的请求方式有POST、PUT、PATCH、DELETE。
# def yes_form(request):
#     from_data = request.POST
#     print(from_data)
#     print(from_data.get("name"))
#     print(from_data.get("school"))
#     print(from_data.get("sc","啦啦啦"))
#     print(from_data.getlist)
#
#     return HttpResponse("可以发送请求体数据的请求方式有POST、PUT、PATCH、DELETE")


#3.2 请求体参数 body 表单类型
# 非表单类型 Non-Form Data  非表单参数 json,js,xml
#body==>bytes.decode==>str
# def no_form(request):
#     #解析 非表单数据的参数 request.boy ===>bytes
#     body_data = request.body
#     print(body_data)
#
#     body_str =body_data.decode()
#     body_dict = json.loads(body_str)
#     print(body_dict)
#     return HttpResponse("非表单类型 Non-Form Data 非表单参数 ")

#4.解析请求头参数 request.META ===>Dict
# def qs_head(request):
#     request_heads = request.META
#     # print(request_heads)
#     # print(request_heads["itcast"]) django自动转换成大写的HTTP_ITCAST
#     #自己测试的时候 助手itcast ===>终端 HTTP_ITCAST
#     print(request_heads['HTTP_ITCAST'])
#     return HttpResponse("解析请求头参数 request.META ===>Dict ")

#5.request其他参数
# def qs_others(request):
#     print("请求方式:",request.method)
#     print("用户:", request.user)
#     print("路径:", request.path)
#     print("编码:", request.encoding)
#
#     return HttpResponse("request其他参数  ")

#6.测试
# def test(request,number):
#     # 都是request的属性
#     print(number)
#     # 666666
#
#     print(request.GET)
#     #<QueryDict: {'a': ['10'], 'b': ['999']}>
#
#     print(request.POST)
#     #<QueryDict: {'a': ['10'], 'b': ['20']}>
#
#     return HttpResponse("测试案例 ")

#7.响应对象
def resp(request):
    #1.参数          响应内容  MIME
    # return HttpResponse(
    #     content="响应对象 ",
    #     #文件交互格式
    #     content_type="text/html;charset=utf8;",
    #     #状态码
    #     status = 200
    #
    # )
    #2.属性
    # response = HttpResponse()
    # response.content ="lalalalalal"
    # response.status_code = 444
    # return response
    #3.子类 JsonResponse()
    #不能传字典,接收默认字符串 可以加 ''' dict_data'''
    dict_data ={
        "name":"秀秀怪",
        "age" :88,
        "school":"多伦多"

    }#字典转字符串   将html.text  变为 application/json
    from django.http.response import JsonResponse
    return JsonResponse(dict_data)
    #safe =False  JsonResponse list==str
    # return JsonResponse(list_data,safe=False)


