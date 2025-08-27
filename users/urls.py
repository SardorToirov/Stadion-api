from django.urls import path
from .views import RegisterViews,ProfileViews,LoginViews
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterViews.as_view(), name="Register"),
    path("login/",LoginViews.as_view(),name="login"),
    path("token/refresh/",TokenRefreshView.as_view(),name="token_refresh"),
    path("profile/",ProfileViews.as_view(),name="profile")
]
