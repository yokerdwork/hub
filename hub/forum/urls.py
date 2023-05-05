from django.conf.urls.static import static
from django.urls import path

from hub import settings
from .views import *

urlpatterns = [
    path('', index),  #http://127.0.0.1:8000/
    path('forum/<int:forumid>/', forum), #http://127.0.0.1:8000/forum/1/
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
