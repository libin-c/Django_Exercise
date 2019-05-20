from django.conf.urls import url

from Bclassview.views import the_decorator
from . import views

urlpatterns = [
    # url(r'^rubbish/', views.rubbishView.as_view()),
    # 好麻烦
    # url(r'^rubbish/', the_decorator(views.rubbishView.as_view())),
    url(r'^rubbish/', views.rubbishView.as_view()),
]
