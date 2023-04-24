from django.urls import path

from .views import *

urlpatterns = [
    path('', index),  #http://127.0.0.1:8000/
    path('forum/<int:forumid>/', forum), #http://127.0.0.1:8000/forum/1/
]