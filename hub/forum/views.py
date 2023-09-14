from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *
from template_hub.models import *

# Create your views here.
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Документация", 'url_name': 'forum_start'},
        {'title': "Обратная связь", 'url_name': 'feed_back'},
        {'title': "Войти", 'url_name': 'login'}
]
def index(request):
    posts = forum.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
    }
    return render(request, 'forum/index.html', context=context)

def about(request):
    return render(request, 'forum/about.html', {'menu': menu, 'title': 'О проекте'})

def forum_start_page(request, forumid):
    return HttpResponse(f'<h1>Страница форум</h1><p>{forumid}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена: 404</h1>')

def forum_start(request):
    context = {
        'menu': menu,
        'title': 'Документация',
    }
    return render(request, 'forum/forumstart.html', context=context)

def login(request):
    return HttpResponse('Вход в систему')

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')

def template_hub(request):
    context = {
        'menu': menu,
        'title': 'Шаблоны',
    }
    return render(request, 'forum/templatehub.html', context=context)

def legal_calendar(request):
    context = {
        'menu': menu,
        'title': 'Судебный календарь',
    }
    return render(request, 'forum/legalcalendar.html', context=context)
def create_client(request):
    context = {
        'menu': menu,
        'title': 'Картотека',
    }
    return render(request, 'forum/create_client.html', context=context)

def feedback(request):
    context = {
        'menu': menu,
        'title': 'Обратная связь',
    }
    return render(request, 'forum/feedback.html', context=context)
