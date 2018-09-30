from django.shortcuts import render, get_object_or_404

from blog.models import *


class ObjectDetailMixin:
    model = None
    template = None
    url_post_update = False

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__exact=slug)
        return render(request, self.template, {self.model.__name__.lower(): obj,
                                               'url_post_update': self.url_post_update,
                                               'admin_object': obj})
