from django.shortcuts import render
from .models import Booking
from .seializers import BookingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

# Create your views here.

# GET
class ListBookingView(APIView):
    def get(self,request):
        booking = Booking.objects.all()
        serializers = BookingSerializer(booking,many=True)
        return Response(serializers.data)

# POST
@extend_schema(request=BookingSerializer)
class CreateBookingView(APIView):
    def post(self,request):
        serializers = BookingSerializer(data=request.data)
        print(request.user)
        if serializers.is_valid():
            stadium = serializers.validated_data["stadium"]
            day = serializers.validated_data["day"]
            start_time = serializers.validated_data["start_time"]
            end_time = serializers.validated_data["end_time"]

            conflicting_orders = Booking.objects.filter(stadium_id=stadium,
                                                        day=day,
                                                        start_time__lt=end_time,
                                                        end_time__gt=start_time)
            if conflicting_orders:
                return Response({"Errors":"Bu  stadion shu vaqda allaqachon band qilingan!!"},status=status.HTTP_400_BAD_REQUEST)
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


    