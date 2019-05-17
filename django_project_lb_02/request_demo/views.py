from django.shortcuts import render
from django.http.response import HttpResponse
import json
# Create your views here.

# 1.0   路径拼接
def request_path(request , operate , content):
    return  HttpResponse("您打开的网页网址是%s/%s" %(operate,content))


# 2.0   查询字符串
def request_select(request):
    ret = request.GET
    return  HttpResponse('您GET发送的字符串是：姓名: %s  年龄: %s  爱好：%s'%(ret.get('name'),ret.get('age'),ret.getlist('hobby')))


# 3.0   请求体 3.1 form 表单提交
def request_form(request):
    ret = request.POST
    print(ret)
    return HttpResponse('您POST发送的字符串是：账号: %s  密码: %s  爱好：%s' % (ret.get('num'), ret.get('pwd'), ret.getlist('hobby')))
# 3.2   请求体 json 表单提交
def request_json(request):
    ret = request.body
    print(json.loads(ret))
    print(type(json.loads(ret)))
    return HttpResponse('您JSON发送过来的字符串是：%s'%ret.decode('utf-8'))

# 3.2   请求体 list 表单提交
def request_list(request):
    ret = request.body
    print(ret.decode())
    print(json.loads(ret))
    print(type(json.loads(ret)))
    return HttpResponse('您JSON发送过来的字符串是：%s'%json.loads(ret))

# 4.0 请求头
def request_head(request):
    ret = request.META
    print(ret)
    print(ret['HTTP_LIBIN'])
    print('请求方式',request.method)
    print('用户',request.user)
    print('请求路径',request.path)
    print('编码',request.encoding)
    return HttpResponse('您通过head请求头发过来的字符串是:%s  \r\n  %s'%(ret,ret['HTTP_LIBIN']))
    #return HttpResponse('请求方式:%s\r\n 请求用户：%s\r\n请求路径：%s\r\n请求编码：%s' %(request.method,request.user,request.path,request.encoding))


   # HttpResponse 其他属性
   # request.method       请求方式
   # request.user         用户
   # request.path         请求路径
   # request.encoding     编码 None utf8