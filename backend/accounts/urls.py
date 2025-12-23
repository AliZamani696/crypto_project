from django.urls import path
from . import views

urlpatterns = [
        path("watchlist/",views.WatchListListCreateAPI.as_view(),name="watchlist-list-create"),
]