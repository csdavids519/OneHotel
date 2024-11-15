from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Room, Booking
from .forms import BookingForm

import string, random

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
    print('room query:',room_type_query,
          'bed query:',bed_type_query,
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

# https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
def create_booking_code():
    booking_code = ''.join(random.choices(string.ascii_uppercase, k=5))
    print(booking_code)
    return booking_code


def room_detail(request, room_number):
    qs = Room.objects.all()
    room = get_object_or_404(qs, room_number=room_number)
    room_type = room.room_type
    floor = room.floor
    bed_type = room.bed_type
    view =room.view
    booking_form = BookingForm

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.booking_code = create_booking_code()
            booking.user_name = request.user
            booking.room_number = room_number
            booking.room_info = room
            booking_form.save()
            messages.add_message(request, messages.SUCCESS, f"SUCCESS! Your booking request has been submitted for approval. Booking code: {booking.booking_code}")
   
    return render(
        request, "room_detail.html",
        {
            'room_number': room,
            'room_type': room_type,
            'floor': floor,
            'bed_type': bed_type,
            'view': view,
            'booking_form': booking_form,
        }
    )

def UserBookings(request):
    queryset = Booking.objects.filter(user_name=request.user)
    print(queryset)
    return render(request, "user_bookings.html", {'booking': queryset})


def booking_edit(request, booking_code):
    booking = get_object_or_404(Booking, booking_code=booking_code, user_name=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('user_booking')
        
    else:
        form = BookingForm(instance = booking)

    return render(request, 'edit_booking.html', {'form': form, 'booking': booking})
