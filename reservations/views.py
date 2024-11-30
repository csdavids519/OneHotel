from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Room, Booking
from .forms import BookingForm

import string
import random

# Create your views here.


def FilterList(request):
    """
    Filters for the searched rooms.
    Collect all Room objects to 'qs' queryset,
    use a filter to check for each query request from the user

    render the resulting qs list to room_search.html

    Code Reference: Matt Freire from YouTube see Read Me for detail.
    """
    # collet basic room model data to display page
    qs = Room.objects.all()
    room_type_query = request.GET.get('room_type', '')
    bed_type_query = request.GET.get('bed_type', '')
    view_type_query = request.GET.get('view_type', '')

    # Collect all filter parameters from the filter request
    if request.GET:
        qs = Room.objects.all()

    # filter for room types
    if room_type_query != "Any":
        qs = qs.filter(room_type=room_type_query)

    # filter for bed types
    if bed_type_query != "Any":
        qs = qs.filter(bed_type=bed_type_query)

    # filter for view types
    if view_type_query != "Any":
        qs = qs.filter(view=view_type_query)

    context = {
        'queryset': qs
    }

    return render(request, "room_search.html", context)


def create_booking_code():
    """
    Create a randomized code of five uppercase letters

    Code Reference: stackoverflow string generation see Read Me for detail.
    """
    booking_code = ''.join(random.choices(string.ascii_uppercase, k=5))

    return booking_code


def room_detail(request, room_number):
    """
    Display detailed room information based on room number selected.
    collect all data from Room model and BookingForm and render a card
    with the room details.

    Accept POST requests for room booking, check form is valid and
    set success messages.
    """
    qs = Room.objects.all()
    room = get_object_or_404(qs, room_number=room_number)
    room_type = room.room_type
    floor = room.floor
    bed_type = room.bed_type
    view = room.view
    booking_form = BookingForm

    # wait for POST request from BookingForm
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)

        # check form is valid and set room data to booking
        # data with new booking code
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.booking_code = create_booking_code()
            booking.user_name = request.user
            booking.room_number = room_number
            booking.room_info = room
            booking_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "SUCCESS! Your booking request has been"
                "submitted for approval!"
            )
            messages.add_message(
                request, messages.SUCCESS,
                "View your booking status on the User"
                f"Bookings page. Booking code: {booking.booking_code}"
            )

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
    """
    Check Booking data for all bookings with same username
    """
    queryset = Booking.objects.filter(user_name=request.user)

    return render(request, "user_bookings.html", {'booking': queryset})


def booking_edit(request, booking_code):
    """
    Allows users to edit the dates on open bookings.
    Based on username and booking code.
    """
    booking = get_object_or_404(
        Booking,
        booking_code=booking_code,
        user_name=request.user
    )
    # check if booking is already approved
    if booking.status == 'APPROVED':
        messages.add_message(
            request,
            messages.WARNING,
            "SORRY! Your booking is already approved, "
            "please contact support to modify your booking"
        )

        return redirect('user_booking')
    else:
        # if edit is made redirect to 'user_booking'
        if request.method == 'POST':
            form = BookingForm(request.POST, instance=booking)
            if form.is_valid():
                form.save()
                return redirect('user_booking')

        # if no bookings are made, display existing BookingForm data
        else:
            form = BookingForm(instance=booking)

        return render(
            request,
            'edit_booking.html',
            {'form': form, 'booking': booking}
        )


def delete_booking(request, booking_code):
    """
    Allows users to delete a booking if the status is not set to 'approved'
    Sets information messages based on deletion or if delete was denied.
    """
    booking = get_object_or_404(Booking, booking_code=booking_code)

    if booking.status == 'APPROVED':
        messages.add_message(
            request,
            messages.WARNING,
            "SORRY! Your booking is already approved, "
            "please contact support to modify your booking"
        )
    else:
        booking.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            "Your booking has been deleted"
        )

    return redirect('user_booking')
