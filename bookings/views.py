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
        print("SALOM")
        serializers = BookingSerializer(data=request.data)
        print(request.user)
        if serializers.is_valid():
            stadium = serializers.validated_data["stadium"]
            day = serializers.validated_data["day"]
            start_time = serializers.validated_data["start_time"]
            end_time = serializers.validated_data["end_time"]

            conflict =Booking.objects.filter(
                stadium=stadium,
                day=day,
                status="confirmed",
                start_time=start_time,
                end_time=end_time
            ).exists()
            if conflict:
                return Response({"Errors":"Bu  stadion shu vaqda allaqachon band qilingan!!"},status=status.HTTP_400_BAD_REQUEST)


            serializers.save(request=request.user)
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


    