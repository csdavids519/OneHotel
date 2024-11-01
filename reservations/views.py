from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Room

# Create your views here.

class RoomsList(generic.ListView):
    queryset = Room.objects.filter(room_type=1)
    template_name = "index.html" 
    paginate_by = 6
