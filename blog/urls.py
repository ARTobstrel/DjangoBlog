from django.urls import path

from .views import *

urlpatterns = [
    path('', post_list, name='post_list'),
    # path('post/<str:slug>/', post_detail, name='post_detail'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('tags/', tags_list, name='tags_list'),
    # path('tag/<str:slug>', tag_detail, name='tag_detail')
    path('tag/<str:slug>', TagDetail.as_view(), name='tag_detail')
]