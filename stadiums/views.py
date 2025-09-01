from rest_framework.generics import (
    CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from .models import Stadium
from .serializers import StadiumSerializer
from .permissions import IsOwnerCreated


class StadionCreateView(CreateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StadionListView(ListAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer


class StadionUpdateView(UpdateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = [IsOwnerCreated]


class StadionDeleteView(DestroyAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = [IsOwnerCreated]
