from django.shortcuts import render, get_object_or_404, redirect

from meetings.forms import MeetingForm
from meetings.models import Meetings, Room


def detail(request, id):
    meeting = get_object_or_404(Meetings, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def all_meetings(request):
    meetings = Meetings.objects.all()
    return render(request, "meetings/all.html", {"meetings": meetings})


def all_rooms(request):
    rooms = Room.objects.all()
    return render(request, "meetings/rooms.html", {"rooms": rooms})


def room(request, id):
    roomer = get_object_or_404(Room, pk=id)
    return render(request, "meetings/room.html", {"room": roomer})


def new(request):
    if request.method == "POST":
        # post hase been submitted
        form = MeetingForm(request.POST)
        if form.is_valid():  # checked if valid data were submitted
            form.save()
            return redirect('home')
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})
