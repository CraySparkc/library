from django.http import HttpResponseRedirect
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
        is_staff = request.POST.get('is-staff')
        username = request.POST.get('username')
    else:
        return HttpResponseRedirect(reverse('register'))


