"""django_project_lsc_01 URL Configuration

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
#导视图函数的包
from Auser import views
urlpatterns = [
    #admin后台管理站点，系统自带的
    url(r'^admin/', admin.site.urls),

    #1.总路由 ---子应用视图函数
    # url(r'^login/', views.index),

    #2.总路由-子路由
    url(r'^Ausers/', include('Auser.urls')),
    #3.路由屏蔽-总路由-子路由
    # 总路由起名 见名知意
    url(r'^Busers/', include('Buser.urls',namespace="Busers")),


]
