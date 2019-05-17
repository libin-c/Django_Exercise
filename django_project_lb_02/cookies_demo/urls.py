from django.conf.urls import url
from django.contrib import admin
from .import views


urlpatterns = [


    # url(r'^request/$', views.request_select),
    url(r'^/?$', views.cookies_demo),

]