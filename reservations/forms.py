from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('reserved_start_date', 'reserved_end_date',)
        widgets = {
            'reserved_start_date':
            forms.DateInput(attrs={'required': 'required', 'type': 'date'}),
            'reserved_end_date':
            forms.DateInput(attrs={'required': 'required', 'type': 'date'}),
        }

    reserved_start_date = forms.DateField(required=True)
    reserved_end_date = forms.DateField(required=True)
