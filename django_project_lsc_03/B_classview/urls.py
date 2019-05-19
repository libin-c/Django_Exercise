from django.conf.urls import url
from django.contrib import admin
from . import views
from B_classview.views import my_decorator

urlpatterns = [

    # url(r'^',views.handTest)
    # 2. 子路由-类视图-->视图函数
    # url(r'^',views.AutomaticTest.as_view())
    # 3. 给类视图 --函数  --添加装饰器
    #灵魂写法 func = my_decorator(func)
    # url(r'^',my_decorator(views.AutomaticTest.as_view()))

    # 4.装饰器 添加到类 上
    # url(r'^',(views.AutomaticTest.as_view()))

    #5.扩展类
    url(r'^',(views.LoginMixin.as_view()))

]
