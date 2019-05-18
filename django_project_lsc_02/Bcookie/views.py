from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json
#cookies KV
def cookies(request):
    #1.设置cookie
    # response = JsonResponse({"KEY":"VALUE"})
    # response_0 = JsonResponse({"GM": "MU"})
    response_2 = HttpResponse()
    response_3 = HttpResponse({"GM": "MU"})
    # 1.设置cookie  key,value
    # 过期时间
    # response.set_cookie("master","xiuixuguai",max_age=600)
    # response_0.set_cookie("master", "zzg", max_age=600)
    response_2.set_cookie("xxg","9494213")
    response_3.set_cookie("zzg", "00944")
    #2.读取cookie 校验if
    result = request.COOKIES
    user =result.keys()
    print(user)

    if "xxg" in user:
        print("xxg的密码是:%s" % result.get("xxg"))
        return HttpResponse("xxg的密码是:%s" % result.get("xxg"))
        # return response_2.write("xxg的密码是:%s" % result.get("xxg"))


    # print(type(result))
    print(result)
    #3.删除
    # response.delete_cookie("master")
    return response_2
