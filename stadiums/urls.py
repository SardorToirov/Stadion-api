from django.urls import path
from stadiums.views import (
    StadionCreateView,
StadionListView


)

urlpatterns = [
    path('create/', StadionCreateView.as_view()),
    path('list/',StadionListView.as_view())
    # path('list/', StadionListView.as_view(), name='stadium-list'),
    # path('update/<int:pk>/', StadionUpdateView.as_view(), name='stadium-update'),
    # path('delete/<int:pk>/', StadionDeleteView.as_view(), name='stadium-delete'),
]
