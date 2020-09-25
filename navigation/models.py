from django.db import models

# Create your models here.


class Place(models.Model):
    fond = models.CharField(max_length='30', verbose_name='Фонд')
    cab_number = models.IntegerField(verbose_name='Номер кабинета')
    cab_name = models.CharField(max_length=50, verbose_name='Название отдела')