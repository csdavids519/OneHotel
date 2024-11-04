from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Room, Booking
from datetime import datetime

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



    #     if booking.reserved_start_date > check_out or booking.reserved_end_date < check_in:
    #         availability_list.append(True)
    #     else:
    #         availability_list(False)
    # return all(availability_list) #returns true when all items in availability_list are true






# ref Matt Freire
# ref booking check DarshanDev
def FilterList(request):
    qs = Room.objects.all()
    room_type_query = request.GET.get('room_type')
    bed_type_query = request.GET.get('bed_type')
    check_in_query = request.GET.get('date_check_in')
    check_out_query = request.GET.get('date_check_out')




    # check room is available if dates are selected
    if check_in_query and check_out_query:
        # Get available rooms from the check_availability function
        available_rooms = check_availability(check_in_query, check_out_query)
        # Print the list of available rooms to the console
        print("Available Rooms:", available_rooms)
        # Filter the queryset to only include the available rooms
        qs = qs.filter(id__in=[room.id for room in available_rooms])


    # if room_type_query and bed_type_query:
    #     qs = qs.filter( 
    #         room_type__icontains=room_type_query,
    #         bed_type__icontains=bed_type_query
    #     )

    # elif room_type_query:
    #     qs = qs.filter(room_type__icontains=room_type_query)

    # elif bed_type_query:
    #     qs = qs.filter(bed_type__icontains=bed_type_query)

    context = {
        'queryset': qs
    }

    return render(request, "index.html", context)



# def FilterList(request):
#     qs = Room.objects.all()
    
#     # Collect all filter parameters from the request
#     room_type_query = request.GET.get('room_type', '').strip()
#     bed_type_query = request.GET.get('bed_type', '').strip()
#     price_query = request.GET.get('price', '').strip()
#     availability_query = request.GET.get('availability', '').strip()
#     guest_capacity_query = request.GET.get('guest_capacity', '').strip()

#     # Create a dictionary for filtering based on the provided parameters
#     filter_params = {}

#     if room_type_query:
#         filter_params['room_type__icontains'] = room_type_query
#     if bed_type_query:
#         filter_params['bed_type__icontains'] = bed_type_query
#     if availability_query:
#         filter_params['availability__icontains'] = availability_query

#     # Apply all filters at once
#     if filter_params:
#         qs = qs.filter(**filter_params)

#     context = {
#         'queryset': qs
#     }

#     return render(request, "index.html", context)

