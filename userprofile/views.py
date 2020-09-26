from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import logout
from django.shortcuts import redirect
from django.urls import reverse

from navigation import views

# Create your views here.


def profile(request):
    return render(request, 'userprofile/profile.html', context={})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Bad!!!")
        else:
            return HttpResponse('Аккаунт заблокирован')
    else:
        return HttpResponseRedirect(reverse('index'))


