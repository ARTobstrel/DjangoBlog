from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def post_list(request):
    a = request
    return render(request, 'blog/index.html', {'request': a, 'req_dir': dir(request)})
