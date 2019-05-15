"""django_project_lb_01 URL Configuration

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
from users import  views

urlpatterns = [
    # 这是 系统路由
    url(r'^admin/$', admin.site.urls),
    # 这里是index 路由
    url(r'^index/$', views.index),
    # 1.这里是总路
    url(r'^demo/', include('users.urls')),
    # 2. 和利时redirect的路由
    url(r'^redirect/', include('redirect_demo.urls',namespace='redirect')),
]
