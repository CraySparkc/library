from django.shortcuts import render

# Create your views here.


def index(request):
    cont = {'message': 'Nice try'}
    return render(request, 'index.html', context=cont)