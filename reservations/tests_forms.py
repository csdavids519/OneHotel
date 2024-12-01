from django.test import TestCase
from .forms import BookingForm

# Create your tests here.


class TestBookingForm(TestCase):

    # code reference: Code Institute Django Blog test_forms.py
    def test_form_is_valid(self):
        """ Test for  all fields """
        form = BookingForm(
            {'reserved_start_date': '2024-12-01',
             'reserved_end_date': '2024-12-10'})
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_wrong_format(self):
        """ Test for wrong date format """
        form = BookingForm(
            {'reserved_start_date': '01-12-2024',
             'reserved_end_date': '2024-12-10'})
        self.assertFalse(
            form.is_valid(), msg="Wrong date format was given")
