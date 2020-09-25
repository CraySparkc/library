from django.db import models
from navigation.models import Place

class event(models.model):
    name=models.CharField('Название' , max_length=50)
    desc=models.TextField('Описание')
    date=models.DateTimeField('Дата публикации' , auto_created=False)
    theme=models.ForeignKey(theme)
    place=models.ForeignKey(Place)
    organizer=models.CharField('Организатор' , max_length=100)
    photo=models.ImageField('Фото' , upload_to='photo_event' , blank=True)

class theme(models.model):
    theme=models.CharField('Тема' , auto_created=50)

