from django.urls import path
from .views import ListBookingView,CreateBookingView,BookingStadion,IntermediateBooking

urlpatterns = [
    path('list/',ListBookingView.as_view()),
    path('create/',CreateBookingView.as_view()),
    path('bronlist/',BookingStadion.as_view()),
    path('brontime/<str:start_time>/<str:end_time>/',IntermediateBooking.as_view())
]

