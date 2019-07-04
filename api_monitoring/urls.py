from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    #path('url', name of function of views, op: name)
]