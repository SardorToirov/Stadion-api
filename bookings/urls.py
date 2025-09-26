from django.urls import path
from .views import ListBookingView,CreateBookingView,BookingStadion

urlpatterns = [
    path('bronlist/',BookingStadion.as_view()),
    path('list/',ListBookingView.as_view()),
    path('create/',CreateBookingView.as_view())
]

