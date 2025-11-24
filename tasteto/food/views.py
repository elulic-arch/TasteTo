from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Place


class PlaceListView(ListView):
    model = Place
    template_name = "food/place_list.html"
    context_object_name = "places"
    ordering = ["name"]


class PlaceDetailView(DetailView):
    model = Place
    template_name = "food/place_detail.html"
    context_object_name = "place"


class PlaceCreateView(CreateView):
    model = Place
    template_name = "food/place_form.html"
    fields = ["name", "description", "address", "rating", "image"]
    success_url = reverse_lazy("food:place_list")


class PlaceUpdateView(UpdateView):
    model = Place
    template_name = "food/place_form_update.html"
    fields = ["name", "description", "address", "rating", "image"]
    context_object_name = "place"
    success_url = reverse_lazy("food:place_list")


class PlaceDeleteView(DeleteView):
    model = Place
    template_name = "food/place_confirm_delete.html"
    context_object_name = "place"
    success_url = reverse_lazy("food:place_list")
