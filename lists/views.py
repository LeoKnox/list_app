from django.shortcuts import render

from .models import My_List, Sub_List
from .forms import ListForm

def index(request):
    lists = My_List.objects.values()
    return render(request, 'index.html', {'lists': lists})

def create(request):
    context = {}

    form = ListForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'create.html', context)