from django.urls import path
from stadiums.views import StadionViews,StadionViewsList


urlpatterns = [
    path('create/',StadionViews.as_view()),
    path('list/',StadionViewsList.as_view())
]
