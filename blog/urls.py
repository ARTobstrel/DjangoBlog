from django.urls import path

from .views import *

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<str:slug>/', post_detail, name='post_detail'),
]