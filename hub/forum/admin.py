from django.contrib import admin

from .models import *


class forumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'published_status')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('published_status',)
    list_filter = ('published_status', 'time_create')


admin.site.register(forum, forumAdmin)
