from django.db import models

# Create your models here.
class forum(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=False)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    published_status = models.BooleanField(default=True)
    comment = models.TextField(blank=False)
    comment_time_create = models.DateTimeField(auto_now_add=True)
    comment_time_update = models.DateTimeField(auto_now=True)
    comment_photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
