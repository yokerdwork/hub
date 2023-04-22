from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Страница приложения форум')

def forum(request):
    return HttpResponse('Страница приложения форум')
