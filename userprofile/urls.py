from django.urls import path
from userprofile import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('logout/', views.user_logout, name="logout"),
    path('login/', views.user_login, name="login")
]