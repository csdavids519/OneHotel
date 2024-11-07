from . import views
from django.urls import path

urlpatterns = [
    path('', views.FilterList, name="FilterList"),
    path('roomdetail/<int:room_number>/', views.room_detail, name="room_detail"),
]