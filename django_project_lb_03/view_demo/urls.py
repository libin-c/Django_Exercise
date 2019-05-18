from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    # 视图函数路由
    # url(r'^', views.view_demo),

    # 类视图路由
    # url(r'^', views.ViewDemo.as_view()),

    # 类视图Mixin扩展类
    url(r'^', views.ClassViewDemo.as_view()),

]