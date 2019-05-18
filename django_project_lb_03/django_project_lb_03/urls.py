"""django_project_lb_03 URL Configuration

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
from django.conf.urls import url , include
from django.contrib import admin
from session_demo import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # session 总路由
    url(r'^session/', include('session_demo.urls')),
    # view 总路由 类视图
    url(r'^view/', include('view_demo.urls')),
    # classview 总路由 类视图 装饰器
    url(r'^classview/', include('class_view_demo.urls')),

    url(r'^templates', views.TemplatesDemo.as_view()),
]
