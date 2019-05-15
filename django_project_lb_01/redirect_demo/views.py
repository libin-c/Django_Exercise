from django.shortcuts import render ,redirect
from django.http.response import HttpResponse
from  django.urls import reverse
# Create your views here.
def Routing(request):
    return HttpResponse(' 我是路由 我被屏蔽了')
def Routing_mask(request):
    return  redirect(reverse('child'))