from django.shortcuts import render
from django.contrib.auth.views import logout
from django.shortcuts import redirect

# Create your views here.


def profile(request):
    return render(request, 'userprofile/profile.html', context={})


def logout(request):
    logout(request)
    return redirect('views.index')
