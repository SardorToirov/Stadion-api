from rest_framework.generics import (
    CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from .models import Stadium
from .serializers import StadiumSerializer
from .permissions import IsOwnerCreated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from drf_spectacular.utils import extend_schema

class StadionListView(APIView):
    def get(self,request):
        stadiums = Stadium.objects.all()
        serializers = StadiumSerializer(stadiums,many=True)

        return Response(serializers.data)

@extend_schema(request=StadiumSerializer)
class StadionCreateView(APIView):

    def post(self, request):

        if request.user.role != "owner":
            raise ValidationError({"errors":"owner bilan kiring!"})

        serializer = StadiumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class StadionListView(ListAPIView):
#
#
# class StadionUpdateView(UpdateAPIView):
#
#
#
# class StadionDeleteView(DestroyAPIView):

