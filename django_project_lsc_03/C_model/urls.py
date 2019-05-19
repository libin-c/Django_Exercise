from django.conf.urls import url
from django.contrib import admin
from . import views
from B_classview.views import my_decorator

urlpatterns = [

    # url(r'^',views.index),

    # url(r'^',views.indexView.as_view()),

    # url(r'^',views.index2),

    url(r'^',views.index3)
]
