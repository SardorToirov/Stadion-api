from django.contrib.auth import get_user_model
from rest_framework import generics,permissions
from .serializers import UserSerializer ,LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login
User = get_user_model()



class ProfileViews(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema(request=LoginSerializer)
class LoginView(APIView):
    def post(self, request):
        username = request.data["username"]
        print(username)
        password = request.data["password"]


        user = authenticate(username=username, password=password)
        if not user:
            return Response({"error": "Username yoki parol noto‘g‘ri!"}, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)
        login(request,user)
        return Response(
            {
                "message": "Login muvaffaqiyatli!",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK
        )

