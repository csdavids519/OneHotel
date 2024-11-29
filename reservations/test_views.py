from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class TestViews(TestCase):

    # code reference: Code Institue Django Blog test_views.py
    def test_correct_template_is_used_filter_list(self):
        """ Test filter list uses the correct template """
        response = self.client.get(reverse('FilterList'))
        self.assertTemplateUsed(response, 'room_search.html')

    def test_correct_template_is_used_user_booking(self):
        """ Test user booking uses the correct template """
        response = self.client.get(reverse('user_booking'))
        self.assertTemplateUsed(response, 'user_bookings.html')
