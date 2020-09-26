from django.db import models

# Create your models here.


class Place(models.Model):
    fond = models.CharField(max_length=30, verbose_name='Фонд')
    cab_number = models.IntegerField(verbose_name='Номер кабинета')
    cab_name = models.CharField(max_length=50, verbose_name='Название отдела')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.fond


class Library(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=150)
    short_name = models.CharField(verbose_name='Аббревиатура', max_length=30)
    desc = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='other', verbose_name='Фото', blank=True)

    class Meta:
        verbose_name = 'Библиотека'
        verbose_name_plural = 'Библиотеки'

    def __str__(self):
        return self.short_name
