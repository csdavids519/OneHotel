from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Booking)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number',
                    'room_type',
                    'floor',
                    'bed_type',
                    'reserved_start_date',
                    'reserved_end_date',
                    'booking_code']
    list_filter = ['room_number',
                    'room_type',
                    'floor',
                    'bed_type',
                    'reserved_start_date',
                    'reserved_end_date',
                    'booking_code']
    show_facets = admin.ShowFacets.ALWAYS






