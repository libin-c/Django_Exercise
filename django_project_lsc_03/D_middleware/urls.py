from django.conf.urls import url
from django.contrib import admin
from . import views
from B_classview.views import my_decorator

urlpatterns = [


    url(r'^',views.simple_middleware),

]
