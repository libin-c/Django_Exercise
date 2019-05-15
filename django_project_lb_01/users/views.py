from django.shortcuts import render ,redirect
from django.http.response import HttpResponse
from django.urls import reverse
# Create your views here.
def index(request):
    return HttpResponse("这是index -----  主界面！")
def indexChild(request):
    return redirect(reverse('redirect:rout'))
