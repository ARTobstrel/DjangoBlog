from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from blog.models import Post, Tag
from blog.utils import ObjectDetailMixin


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', {'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'
