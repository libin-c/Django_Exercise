"""django_project_lsc_02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from Auser import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #beijing/2018
    #1.路径拼接参数
    # url(r'^weather/(?P<city>\w*)/(?P<year>\d{4})/$',views.weather),

    #2.查询字符串Query String---?a=10&b=20&a=30
    #http://127.0.0.1:8000/qs/?a=1&b=2&a=3
    # url(r'^qs/',views.qs),

    #3.1请求体参数 body 可以发送请求体数据的请求方式有POST、PUT、PATCH、DELETE。
    #表单形式  GET没有请求体  只有POST才有 request.POST只能用来获取POST方式的请求体表单数据。
    # url(r'^qsbody/',views.yes_from),

    # 3.2请求体参数
    #非表单类型 Non-Form Data 非表单参数 json,js,xml,html,text
    # body==>bytes.decode==>str
    # url(r'^qsbody/',views.no_form),

    #4.解析请求头参数 request.META ===>Dict
    # url(r'^qshead/',views.qs_head),

    #5.request其他参数
    # url(r'^others/',views.qs_others),

    #6.综合应用案例
    # url(r'^test/(\d+)/$', views.test),

    #7.响应对象
    # url(r'^response/$',views.resp)

    #8.COOKIE
    url(r'^cookie/', include('Bcookie.urls'))
]




