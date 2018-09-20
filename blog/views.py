from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts':posts})

def post_detail(request, slug):
    post = Post.objects.get(slug__exact=slug) #точное соответствие slug
    return render(request, 'blog/post_detail.html', {'post': post})
