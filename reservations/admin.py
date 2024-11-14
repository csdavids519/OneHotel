from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number',
                    'room_type',
                    'floor',
                    'bed_type',
                    'view',
                    ]
    
    list_filter = ['room_number',
                    'room_type',
                    'floor',
                    'bed_type',]
    show_facets = admin.ShowFacets.ALWAYS

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['booking_code',
                    'user_name',
                    'room_number',
                    'status',
                    ]
    
    list_filter = [
                    'room_number',
                ]
    show_facets = admin.ShowFacets.ALWAYS





