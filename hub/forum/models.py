from django.db import models

# Create your models here.
class forum(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    content = models.TextField(max_length=250, blank=False, verbose_name='Текст')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время последней правки')
    published_status = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True)
    json_data = models.JSONField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reversed('post', kwargs={'post_id': self.pk})

    class Category(models.Model):
        name = models.CharField(max_length=100, db_index=True)

        def __str__(self):
            return self.name

    class Meta:
        verbose_name = 'Документация'
        verbose_name_plural = 'Документация'
        ordering = ['time_create', 'time_update', 'title']
        indexes = [
            models.Index(fields=['-title']),
        ]
        #функция индекс сортировки по индексу для ускорения работы БД во время переборки
