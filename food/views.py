from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.shortcuts import render
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add a New Place"
        return context


class PlaceUpdateView(UpdateView):
    model = FoodPlace
    fields = ['name', 'description', 'location', 'category', 'image']
    template_name = "food/place_form_update.html"
    success_url = reverse_lazy("food:place_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Place"
        return context

class PlaceDeleteView(DeleteView):
    model = FoodPlace
    template_name = "food/place_confirm_delete.html"
    success_url = reverse_lazy("food:place_list")


