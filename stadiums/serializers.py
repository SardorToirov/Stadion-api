from rest_framework import serializers
from .models import Stadium
from users.models import User
class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ["id","name","address","price","weight","height","stadions_status"]





