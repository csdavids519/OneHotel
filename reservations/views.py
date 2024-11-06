from django.shortcuts import render
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
    check_in_query = request.GET.get('date_check_in')
    check_out_query = request.GET.get('date_check_out')

    if request.GET:
        qs = Room.objects.all()

    # debug
    print('room query:',room_type_query, 'bed query:',bed_type_query,
          'cin query:',check_in_query, 'cout query:',check_out_query)

    if room_type_query != "Any":
        qs = qs.filter(room_type=room_type_query)
        # debug
        print('room:',qs)

 
    if bed_type_query != "Any":
        qs = qs.filter(bed_type=bed_type_query)
        # debug
        print('bed:',qs)

    context = {
        'queryset': qs
    }

    return render(request, "index.html", context)