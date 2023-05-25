"""
URL configuration for hub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

import template_hub
from forum.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('forum/start', forum_start, name='forum_start'),
    path('feedback', feed_back, name='feed_back'),
    path('login', login, name='login'),
    path('templatehub', template_hub, name='template_hub'),
    path('legalcalendar', legal_calendar, name='legal_calendar'),
    path('cardindex', card_index, name='card_index'),
]

handler404 = pageNotFound
