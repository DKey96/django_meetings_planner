from django.urls import path

from meetings import views

urlpatterns = [
    path("", views.all_meetings, name="meetings"),
    path("<int:id>", views.detail, name="detail"),
    path("rooms", views.all_rooms, name="rooms"),
    path("rooms/<int:id>", views.room, name="room"),
    path("new", views.new, name="newmeeting"),
]
