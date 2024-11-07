from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Room

# Create your views here.
# ref Matt Freire
# ref booking check DarshanDev

def FilterList(request):
    qs = Room.objects.all()
    
    # Collect all filter parameters from the request
    room_type_query = request.GET.get('room_type', '')
    bed_type_query = request.GET.get('bed_type', '')
    view_type_query = request.GET.get('view_type','')

    if request.GET:
        qs = Room.objects.all()

    # debug
    print('room query:',room_type_query, 'bed query:',bed_type_query,
          'view query:', view_type_query
    )


    if room_type_query != "Any":
        qs = qs.filter(room_type=room_type_query)
        # debug
        print('room:',qs)

 
    if bed_type_query != "Any":
        qs = qs.filter(bed_type=bed_type_query)
        # debug
        print('bed:',qs)

    if view_type_query != "Any":
        qs = qs.filter(view=view_type_query)
        # debug
        print('view:',qs)

    context = {
        'queryset': qs
    }

    return render(request, "index.html", context)




def room_detail(request, room_number):
    qs = Room.objects.all()
    room = get_object_or_404(qs, room_number=room_number)
    room_type = room.room_type
    floor = room.floor
    bed_type = room.bed_type
    view =room.view

    return render(
        request, "room_detail.html",
        {
            'room_number': room,
            'room_type': room_type,
            'floor': floor,
            'bed_type': bed_type,
            'view': view,

        }
    )
