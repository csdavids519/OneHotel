from . import views
from django.urls import path

urlpatterns = [
    # path('', views.RoomsList.as_view(), name='RoomsList'),
    # path('roomdetail/',views.room_detail, name="room_detail"),
    path('', views.RoomsList, name="roomlist"),
]