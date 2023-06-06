from django.contrib import admin
from django.urls import path

from template_hub.views import *

urlpatterns = [
    path('templatehub', template_hub, name='template_hub'),
]
