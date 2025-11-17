# food/urls.py
from django.urls import path
from .views import (
    PlaceListView,
    PlaceDetailView,
    PlaceCreateView,
    PlaceUpdateView,
    PlaceDeleteView,   
)

app_name = "food"

urlpatterns = [
    path("", PlaceListView.as_view(), name="place_list"),
    path("place/<int:pk>/", PlaceDetailView.as_view(), name="place_detail"),
    path("place/add/", PlaceCreateView.as_view(), name="place_create"),
    path("place/<int:pk>/edit/", PlaceUpdateView.as_view(), name="place_update"),
    path("place/<int:pk>/delete/", PlaceDeleteView.as_view(), name="place_delete"),
]


