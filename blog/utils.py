from django.shortcuts import render, get_object_or_404

from blog.models import *


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__exact=slug)
        return render(request, self.template, {self.model.__name__.lower(): obj,
                                               'admin_object': obj,
                                               'detail': True})
