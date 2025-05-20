from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return self.name
    

class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название task')
    description = models.TextField(verbose_name='Описание', blank=True)
    is_done = models.BooleanField(verbose_name='Статус задачи', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='category')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.title