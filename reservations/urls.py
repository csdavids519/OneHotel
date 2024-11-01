from . import views
from django.urls import path

urlpatterns = [
    path('', views.RoomsList.as_view(), name='RoomsList'),
]