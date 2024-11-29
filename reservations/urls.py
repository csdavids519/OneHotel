from . import views
from django.urls import path

urlpatterns = [
    path('', views.FilterList, name="FilterList"),
    path('roomdetail/<int:room_number>/',
         views.room_detail,
         name="room_detail"),
    path('useraccount', views.UserBookings, name="user_booking"),
    path('edit/<str:booking_code>/', views.booking_edit, name="edit_booking"),
    path('delete/<str:booking_code>/',
         views.delete_booking,
         name="delete_booking"),
]
