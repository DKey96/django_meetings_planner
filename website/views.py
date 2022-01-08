import datetime

from django.http import HttpResponse
from django.shortcuts import render

from meetings.models import Meetings


def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meetings.objects.all()})


def date(request):
    return HttpResponse(f"It currently {str(datetime.datetime.now())}")


def about(request):
    return HttpResponse(f"I'm Daniel Klic. Software developer/engineer. I'm a star mate!")
