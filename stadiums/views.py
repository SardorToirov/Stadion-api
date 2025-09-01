from django.shortcuts import render
from .models import Stadium
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView
from .serializers import StadiumSerializer
from .permissions import IsOwnerCreated
# Create your views here.


class StadionViews(CreateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = [IsOwnerCreated]


class StadionViewsList(ListAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer


class StadionViewsUpdate(UpdateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = [IsOwnerCreated]


class StadionViewsDelete(DestroyAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = [IsOwnerCreated]
