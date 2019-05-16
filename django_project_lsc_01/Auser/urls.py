# !/usr/bin/env python
# _*_ coding:utf-8 _*_

from django.conf.urls import url
from .import views

urlpatterns = [

    url(r'^Aindex_child/', views.indexChild,name="Ausers-son"),
    url(r'^Aindex/', views.index),
    url(r'^Aindex_xxg/', views.show_xxg),
]
