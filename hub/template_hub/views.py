from django.shortcuts import render

import forum
from forum.views import menu


# Create your views here.
def template_hub(request):
    posts = forum.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Шаблоны',
    }
    return render(request, 'forum/templatehub.html', context=context)