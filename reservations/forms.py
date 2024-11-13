from .models import Booking
from django import forms


class BookingForum(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('reserved_start_date', 'reserved_end_date',)
        widgets = {
            'reserved_start_date': forms.DateInput(attrs={'placeholder': 'Start Date', 'type': 'date'}),
            'reserved_end_date': forms.DateInput(attrs={'placeholder': 'End Date', 'type': 'date'}),
        }