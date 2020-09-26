from django.db import models
from navigation.models import Place, Library


class Theme(models.Model):
    theme = models.CharField('Тема', auto_created=50, max_length=50)

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематик'

    def __str__(self):
        return self.theme


class Event(models.Model):
    name = models.CharField('Название', max_length=50)
    desc = models.TextField('Описание')
    date = models.DateTimeField('Дата публикации', auto_created=False)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, verbose_name='Тематика')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Локация')
    organizer = models.CharField('Организатор', max_length=100)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, verbose_name='Библиотека')
    photo = models.ImageField('Фото', upload_to='photo_event', blank=True)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return str(self.date) + ": " + self.name



