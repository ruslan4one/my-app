from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articles(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Владелец заявки', blank = True, null = True )
    create_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, verbose_name='Автомобиль')
    text = models.TextField(verbose_name='Проблема')
    status = models.BooleanField(verbose_name='Статус заявки', default=False)
    def __str__(self):
        return self.name
    

class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete = models.CASCADE, verbose_name='Заявка', blank = True, null = True,related_name='comments_articles' )
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Автор сообщения', blank = True, null = True )
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Текст сообщения')
