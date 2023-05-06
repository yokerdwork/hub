from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

# Create your views here.
menu = ["Главная страница", "Обновления", "О системе", "Обратная связь", "Войти"]
def index(request):
    return render(request, 'forum/index.html', {'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'forum/about.html', {'menu': menu, 'title': 'О форуме'})

def forum(request, forumid):
    return HttpResponse(f'<h1>Страница форум</h1><p>{forumid}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена: 404</h1>')

