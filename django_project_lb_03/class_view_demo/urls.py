from django.conf.urls import url
from django.contrib import admin

from class_view_demo.views import my_decorator
from . import views

urlpatterns = [
    url(r'^', views.ClassViewDemo.as_view()),



    # # 01. 使用装饰器的第一种方法
    # url(r'^', my_decorator(views.ClassViewDemo.as_view())),

]