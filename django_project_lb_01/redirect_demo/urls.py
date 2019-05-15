from django.conf.urls import url
from django.contrib import admin
from redirect_demo import  views

urlpatterns = [
    # 这是 系统路由
    url(r'^Routing/', views.Routing ,name='rout'),
    # 1.这里是总路由
    url(r'^Routing_mask/', views.Routing_mask ,name='mask'),
]