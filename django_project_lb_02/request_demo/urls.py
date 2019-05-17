from django.conf.urls import url
from django.contrib import admin
from .import views


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # 子路由
    # 1.0   路径拼接
    url(r'^/(?P<operate>[a-zA-Z0-9_]*)/(?P<content>[a-zA-Z0-9_]*)/$', views.request_path),
    # 2.0   查询字符串
    url(r'^/$', views.request_select),

    # 3.0  请求体
    #   3.1  form 表单
    url(r'^/form/?$', views.request_form),
    #   3.2 json xml html 类型
    url(r'^/json/?$', views.request_json),
    #   3.3 json xml html  (list)类型
    url(r'^/list/?$', views.request_list),
    # 4.0  请求头
    url(r'^/head/?$', views.request_head),


]