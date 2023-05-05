from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'forum/index.html')

def about(request):
    return render(request, 'forum/about.html')

def forum(request, forumid):
    return HttpResponse(f'<h1>Страница форум</h1><p>{forumid}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена: 404</h1>')
