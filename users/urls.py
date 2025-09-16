from django.urls import path
from .views import ProfileViews,RegisterView,LoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="Register"),
    path("login/",LoginView.as_view(),name="login"),
    # path("token/refresh/",TokenRefreshView.as_view(),name="token_refresh"),
    path("profile/",ProfileViews.as_view(),name="profile")
]

