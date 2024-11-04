from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Room

# Create your views here.

# class RoomsList(generic.ListView):
#     # queryset = Room.objects.filter(Room=1)
#     template_name = "index.html" 
#     paginate_by = 6


# def room_detail(request):
#     room_number = Room.objects.all()
   
#     context = {'room_number':room_number}

#     return render(request, "room_detail.html", context)
    
# def RoomsList(request):
#     rooms = Room.objects.all()
#     return render(request, "index.html", {"rooms": rooms})


def FilterList(request):
    qs = Room.objects.all()
    room_type_query = request.GET.get('room_type')
    bed_type_query = request.GET.get('bed_type')

    if room_type_query != '' and room_type_query is not None:
        qs = qs.filter(room_type__icontains=room_type_query)

    context = {
        'queryset': qs
    }

    return render(request, "index.html", context)