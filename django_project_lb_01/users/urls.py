
from django.conf.urls import url

from . import views

urlpatterns = [


    # 1. 子路由----> 视图函数
    url(r'^child/', views.indexChild ,name='child'),

]