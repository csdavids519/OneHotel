from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("search/", include("reservations.urls"), name="reservations-urls"),
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),

]
