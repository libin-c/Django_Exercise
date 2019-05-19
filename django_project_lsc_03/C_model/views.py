from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator



class indexView(View):
    def get(self, request):
        # return HttpResponse('模板')
        context = {
            'message': "模板变量{{ k }}"
        }
        return render(request, 'test.html', context=context)


def index(request):
    context={'city': '北京'}
    return render(request,'login.html',context)



def index2(request):
    context = {
        'city': '多伦多',
        'adict': {
            'name': '圣经',
            'author': '神'
        },
        'alist': [1, 2, 3, 4, 5]
    }
    return render(request, 'test2.html', context)



def index3(request):

    return render(request,'timeflsh.html')
