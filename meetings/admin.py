from django.contrib import admin

from meetings.models import Meetings, Room
# Register your models here.

admin.site.register(Meetings)
admin.site.register(Room)
