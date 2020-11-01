from django.shortcuts import render, redirect
from rooms.models import Room
from rooms.forms import RoomForm


def index(request):
    room_data = Room.objects.values()
    return render(request, 'room/index.html', {'rooms': room_data})

def room(request, room_id):
    room_data = Room.objects.filter(id=room_id)
    print(room_data)
    return render(request, 'room/room.html', {'room_data': room_data[0]})

def create(request):
    context = {}

    form = RoomForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/index/')
    context['form'] = form
    return render(request, 'room/create.html', context)

def delete(request, room_id):
    Room.objects.filter(id=room_id).delete()
    return redirect('/index/')

def edit(request, room_id):
    new_room = RoomForm(request.POST or None)
    if new_room.is_valid():
        update = Room.objects.get(id = room_id)
        update.name = request.POST.get('name')
        update.description = request.POST.get('description')
        update.width= request.POST.get('width')
        update.length = request.POST.get('length')
        update.save()
        return redirect('/index/')
    room = Room.objects.get(id = room_id)
    room_data = {
        'name': room.name,
        'description': room.description,
        'width': room.width,
        'length': room.length
    }
    form = RoomForm(initial=room_data)
    return render(request, 'room/edit.html', {'form': form})