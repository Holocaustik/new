from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    picture = models.ImageField(upload_to='portfolio/images', null=True, verbose_name='Изображение')
    url = models.URLField(blank=True, null=True, default='')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Название'
        verbose_name_plural = 'Названия'
