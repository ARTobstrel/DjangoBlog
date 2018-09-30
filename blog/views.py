from django.conf.urls import url
from django.shortcuts import render, redirect
from django.views.generic import View

from blog.forms import TagForm, PostForm
from blog.models import Post, Tag
from blog.utils import ObjectDetailMixin


# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-date_pub')
    return render(request, 'blog/index.html', {'posts': posts})


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_create.html', {'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect('post_list')
        return render(request, 'blog/post_create.html', {'form': bound_form})


class PostUpdate(View):
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = PostForm(instance=post)
        return render(request, 'blog/post_update.html', {'form': bound_form, 'post': post})

    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = PostForm(request.POST, instance=post)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect('post_list')
        return render(request, 'blog/post_update.html', {'form': bound_form, 'post': post})


class PostDelete(View):
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        return render(request, 'blog/post_delete.html', {'post': post})

    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        post.delete()
        return redirect('post_list')


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'
    url_post_update = True


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', {'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect('tags_list')
        return render(request, 'blog/tag_create.html', {'form': bound_form})


class TagUpdate(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForm(instance=tag)
        return render(request, 'blog/tag_update.html', {'form': bound_form, 'tag': tag})

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForm(request.POST, instance=tag)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect('tags_list')
        return render(request, 'blog/tag_update.html', {'form': bound_form, 'tag': tag})


class TagDelete(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        return render(request, 'blog/tag_delete.html', {'tag': tag})

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        tag.delete()
        return redirect('tags_list')


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', {'tags': tags})
