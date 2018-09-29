from django.urls import path

from .views import *

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('tags/', tags_list, name='tags_list'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete'),
    path('tag/create/', TagCreate.as_view(), name='tag_create'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail'),
]
