from django.db import models

# Create your models here.
class template_legal(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=False)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    comment = models.TextField(blank=False)
    comment_time_create = models.DateTimeField(auto_now_add=True)
    comment_time_update = models.DateTimeField(auto_now=True)
