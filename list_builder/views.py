from django.shortcuts import render

from .models import My_List, Sub_List

def index(request):
    lists = My_List.objects.values()
    return render(request, 'index.html', {'lists': lists})

def create(request):
    return render(request, 'create.html')