from django.contrib.auth import get_user_model
from rest_framework import generics,permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer  

User = get_user_model()

class RegisterViews(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViews(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class LoginViews(TokenObtainPairView):
    pass

