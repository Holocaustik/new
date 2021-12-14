from django.db import models


class Post_blogs(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    date = models.DateTimeField(verbose_name='Дата добавления поста')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
