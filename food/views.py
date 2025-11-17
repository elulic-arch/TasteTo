from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import FoodPlace


class PlaceListView(ListView):
    model = FoodPlace
    template_name = "food/place_list.html"
    context_object_name = "places"


class PlaceDetailView(DetailView):
    model = FoodPlace
    template_name = "food/place_detail.html"
    context_object_name = "place"


class PlaceCreateView(CreateView):
    model = FoodPlace
    fields = ['name', 'description', 'location', 'category', 'image']
    template_name = "food/place_form.html"
    success_url = reverse_lazy("food:place_list")


class PlaceUpdateView(UpdateView):
    model = FoodPlace
    fields = ['name', 'description', 'location', 'category', 'image']
    template_name = "food/place_form.html"
    success_url = reverse_lazy("food:place_list")


class PlaceDeleteView(DeleteView):
    model = FoodPlace
    template_name = "food/place_confirm_delete.html"
    success_url = reverse_lazy("food:place_list")
