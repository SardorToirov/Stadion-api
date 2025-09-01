from django.urls import path
from stadiums.views import StadionViews,StadionViewsList,StadionViewsUpdate,StadionViewsDelete


urlpatterns = [
    path('create/',StadionViews.as_view()),
    path('list/',StadionViewsList.as_view()),
    path('update/',StadionViewsUpdate.as_view()),
    path('delete/',StadionViewsDelete.as_view())
]
