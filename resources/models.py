from django.db import models
from navigation.models import Place, Library


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
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название типа')

    class Meta:
        verbose_name = 'Тип ресурса'
        verbose_name_plural = 'Типы ресурса'

    def __str__(self):
        return self.name


class Stack(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Стеллаж'
        verbose_name_plural = 'Стеллажи'

    def __str__(self):
        return self.place.cab_name


class Resource(models.Model):
    inv = models.CharField(max_length=20, verbose_name='ИНВ', unique=True)
    name = models.CharField(max_length=50, verbose_name='Название')
    desk = models.TextField(verbose_name="Описание")
    publishing = models.CharField(max_length=35, verbose_name='Издатель')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name='Автор')
    gener = models.ForeignKey(Gener, on_delete=models.CASCADE, verbose_name='Жанр')
    date = models.DateField(verbose_name='Дата публикации')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Тип ресурса')
    stack = models.ForeignKey(Stack, on_delete=models.CASCADE, verbose_name='Стеллаж')
    library = models.ForeignKey(Library, on_delete=models.CASCADE, verbose_name='Библиотека')
    photo = models.ImageField(upload_to='photo_resource', blank=True, verbose_name='Фото')
    mark = models.CharField(max_length=100, verbose_name='mark')

    class Meta:
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурсы'

    def __str__(self):
        return self.inv + " # " + self.name



