from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def indexCookie(request):
    from django.http.response import JsonResponse
    response = JsonResponse({'key:','cookie'},safe=False)
    response.set_cookie('heima','lsc',max_age=160)
    return response
# 研究可响应对象
# def indexresponse(resquest):
#     # response = HttpResponse()
#     # response.content = '操作属性 '
#     # return response
#     dict_data = {
#         'name':'cxk',
#         'age':'38'
#
#     }
#     from django.http.response import JsonResponse
#     return JsonResponse(dict_data)
# # 加列表  后面加上safe = False
#
# def header_request(request):
#     request_headers = request.META
#     # print(request_headers)
#     # print(request_headers['CONTENT_TYPE'])
#     print('请求方式:',request.method)
#     print('用户:',request.user)
#     print('路径:',request.path)
#     print('编码:',request.encoding)
#     return HttpResponse('解析请求头参数')
#
# def indexBodyNotForm(request):
#
#     body_data = request.body
#     print(body_data)
#     body_str = body_data.decode()
#     print(body_str)
#     return HttpResponse('非表单啊')
# def indexBodyForm(request):
#     form_data = request.POST
#     print(form_data)
#     print(form_data.get('a','默认值'))
#     print(form_data.get('c','默认值'))
#     print(form_data.getlist('a'))
#
#     return HttpResponse('请求体啊')
#
#
#
# def indexQueryPramas(request):
#     # 解析查询的属性
#     Pramas = request.GET
#     print(Pramas)
#     print(Pramas.get('a'))
#     print(Pramas.get('b'))
#     print(Pramas.getlist('a'))
#
#     return HttpResponse('查询特么的参数')
#
#
# def indexJoinPramas(request,city,year):
#     print('城市:', city)
#     print('年份:', year)
#
#     return HttpResponse('shenyang/2019')
#
#
#
# def index(request):
#     return HttpResponse('ouhehe')