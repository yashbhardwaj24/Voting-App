from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Room, RoomMessage, Topic
from .forms import RoomModelForm
from user.utils import paginateProfiles


def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    rooms = Room.objects.filter(  # from child to parent
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    room_count = rooms.count()
    topics = Topic.objects.all()
    RomMessage = RoomMessage.objects.filter(
        Q(room__name__icontains=q) | 
        Q(room__topic__name__icontains=q) 
    )[:4]

    paginator2, custom_range2, rooms = paginateProfiles(
        request, rooms, 4)  # setting up for rooms

    content = {'rooms': rooms, 'topics': topics, 'room_count': room_count,'RomMessage':RomMessage,'paginator2':paginator2,'custom_range2':custom_range2}
    return render(request, 'discord/home.html', content)


def room(request, pk):
    room = Room.objects.get(id=pk)
    # when we have not define in room but child is linked
    RomMessage = room.roommessage_set.all().order_by('created')
    participants = room.participants.all()

    if request.method == 'POST':
        Rmessage = RoomMessage.objects.create(
            user=request.user.profile,
            room=room,
            body=request.POST.get('body')
        )
        
        room.participants.add(request.user.profile)  # .remove()
        return redirect('discord:room', pk=room.id)

    content = {'room': room, 'RoomMessage': RomMessage,
               'participants': participants}
    return render(request, 'discord/room.html', content)


@login_required(login_url='user:login')
def createRoom(request):
    form = RoomModelForm()

    if request.method == 'POST':
        form = RoomModelForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user.profile
            room.save()
            return redirect('discord:Home')

    content = {'form': form}
    return render(request, 'discord/room_form.html', content)


@login_required(login_url='user:login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomModelForm(instance=room)

    print("a", type(request.user), "a")
    print("a", type(room.host), "a")

    if request.user != room.host.user:
        return HttpResponse('You are not allowed 😭')

    if request.method == 'POST':
        form = RoomModelForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('discord:Home')

    content = {'form': form}
    return render(request, 'discord/room_form.html', content)


@login_required(login_url='user:login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host.user:
        return HttpResponse('You are not allowed 😭')

    if request.method == 'POST':
        room.delete()
        return redirect('discord:Home')

    content = {'room': room}
    return render(request, 'discord/delete.html', content)


@login_required(login_url='user:login')
def deleteMessage(request, pk):
    message = RoomMessage.objects.get(id=pk)

    if request.user != message.user.user:
        return HttpResponse('You are not allowed 😭')
    print(message.body)
    if request.method == 'POST':
        message.delete()
        return redirect('discord:room', pk=message.room.id)
        return redirect('discord:Home')

    content = {'room': message}
    return render(request, 'discord/delete.html', content)
