from django.db import models
from navigation.models import Place


# Create your models here.

class Autor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Автор')

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.name


class Gener(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название жанра')


class Type(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название типа')

    class Meta:
        verbose_name = 'Тип ресурса'
        verbose_name_plural = 'Типы ресурса'

    def __str__(self):
        return self.name


class Stack(models.Model):
    place = models.ForeignKey(Place)

    class Meta:
        verbose_name = 'Стеллаж'
        verbose_name_plural = 'Стеллажи'

    def __str__(self):
        return self.place.cab_name


class Resource(models.Model):
    inv = models.CharField(max_length=20, verbose_name='ИНВ')
    name = models.CharField(max_length=50, verbose_name='Название')
    desk = models.TextField(verbose_name="Описание")
    publishing = models.CharField(max_length=35, verbose_name='Издатель')
    autor = models.ForeignKey(Autor)
    gener = models.ForeignKey(Gener)
    date = models.DateField(verbose_name='Дата публикации')
    type = models.ForeignKey(Type)
    stack = models.ForeignKey(Stack)
    photo = models.ImageField(upload_to='photo_resource', blank=True)
    mark = models.CharField(max_length=100, verbose_name='mark')



