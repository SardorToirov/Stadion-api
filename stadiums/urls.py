from django.urls import path
from stadiums.views import (
    StadionCreateView,
    StadionListView,
    StadionUpdateView,
    StadionDeleteView
)

urlpatterns = [
    path('create/', StadionCreateView.as_view()),
    path('list/',StadionListView.as_view()),
    path('update/<int:id>', StadionUpdateView.as_view()),
    path('delete/<int:id>', StadionDeleteView.as_view()),
]
