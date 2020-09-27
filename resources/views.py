from django.core.paginator import Paginator
from django.shortcuts import render
from resources.models import *

# Create your views here.


def index(request):
    return render(request, 'resources/index.html', context={})


def list(requset):
    resourse = Resource.objects.all();
    paginator = Paginator.page(resourse, 1)
    page_number = requset.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(requset, 'resources/list.html', {'page_obj': page_obj, 'resources': resourse})
