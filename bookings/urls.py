from django.urls import path
from .views import ListBookingView,CreateBookingView

urlpatterns = [
    path('list/',ListBookingView.as_view()),
    path('create/',CreateBookingView.as_view())
]