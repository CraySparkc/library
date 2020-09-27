from django.urls import path
from resources import views


urlpatterns = [
    path('', views.index, name="index"),
    path('list/', views.list, name='list'),
]