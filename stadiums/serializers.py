from rest_framework import serializers
from .models import Stadium


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ["id", "name", "owner", "address", "price", "weight", "height", "stadions_status"]
        extra_kwargs = {
            "owner": {"read_only": True}  # owner API orqali kiritilmaydi
        }
