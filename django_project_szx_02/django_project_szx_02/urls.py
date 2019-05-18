"""django_project_szx_02 URL Configuration

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
from Auser import  views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Auser/', include('Auser.urls')),
    # url(r'^login/', views.indexQueryPramas , name='query'),
    # url(r'^login/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.indexJoinPramas),
#     请求体 body    form表单的参数
#     url(r'^login/', views.indexBodyForm , name='form'),
#     url(r'^login/', views.indexBodyNotForm , name='notform'),
#     url(r'^login/', views.header_request , name='headers'),
#     url(r'^response/', views.indexresponse , name='headers'),
        url(r'^', include('bullshit.urls' , namespace ='bullshit')),


]
