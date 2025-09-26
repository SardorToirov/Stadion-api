from rest_framework import serializers
from .models import Booking
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


# class BookingTimeSerializer(serializers):
#     class Meta:
#         model = Booking
#         field = ["start_time","end_time"]