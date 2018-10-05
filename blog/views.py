from django.contrib.auth.mixins import \
    LoginRequiredMixin  # Этот класс нужен для проверки идентификации пользователя. Если пользователь не авторизован, то не  будет перехода по url
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import View

from blog.forms import TagForm, PostForm
from blog.models import Post, Tag
from blog.utils import ObjectDetailMixin
from django.db.models import Q


# Create your views here.
def post_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query)) #филтр поиска по названию или по телу поста
    else:
        posts = Post.objects.all()
    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url
    }

    return render(request, 'blog/index.html', context)


class PostCreate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        form = PostForm()

        return render(request, 'blog/post_create.html', {'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect('post_list')
        return render(request, 'blog/post_create.html', {'form': bound_form})


class PostUpdate(LoginRequiredMixin, View):
    raise_exception = True

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


class PostDelete(LoginRequiredMixin, View):
    raise_exception = True

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


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', {'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect('tags_list')
        return render(request, 'blog/tag_create.html', {'form': bound_form})


class TagUpdate(LoginRequiredMixin, View):
    raise_exception = True

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


class TagDelete(LoginRequiredMixin, View):
    raise_exception = True

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
