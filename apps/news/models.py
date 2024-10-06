from django.db import models

# Create your models here.

class News(models.Model):
    time = models.CharField(max_length=155, verbose_name='Дата')
    title = models.CharField(max_length=155, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание новостей', default='Описание новостей')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name=""
        verbose_name_plural="Новости"