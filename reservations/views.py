from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Room, Booking
from datetime import datetime

# Create your views here.
# ref Matt Freire
# ref booking check DarshanDev

def check_availability(check_in, check_out):
    available_rooms_list=[]
    existing_bookings = Booking.objects.all()
    check_in = datetime.strptime(check_in, "%Y-%m-%d").date()
    check_out = datetime.strptime(check_out, "%Y-%m-%d").date()

    for booking in existing_bookings:
        is_available = True
        for booking in existing_bookings:
           if not (booking.reserved_start_date > check_out or booking.reserved_end_date < check_in):
                is_available = False
                break  # No need to check further if one booking conflicts

        if is_available:
            available_rooms_list.append(booking.room_number)
    print(available_rooms_list)
    return available_rooms_list


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


    if check_in_query and check_out_query:
        available_rooms = check_availability(check_in_query, check_out_query)
        # Filter queryset to include only available rooms
        qs = qs.filter(id__in=available_rooms)

        # debug
        print('date:',qs)


    context = {
        'queryset': qs
    }

    return render(request, "index.html", context)