
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.edit import FormView

from .models import FoodPlace


class PlaceListView(ListView):
    model = FoodPlace
    template_name = "food/place_list.html"
    context_object_name = "places"
    ordering = ["name"]


class PlaceDetailView(DetailView):
    model = FoodPlace
    template_name = "food/place_detail.html"
    context_object_name = "place"


class PlaceCreateView(LoginRequiredMixin, CreateView):
    model = FoodPlace
    fields = ["name", "address", "description", "rating", "image"]
    template_name = "food/place_form.html"
    success_url = reverse_lazy("food:place_list")
    login_url = "login"


class PlaceUpdateView(LoginRequiredMixin, UpdateView):
    model = FoodPlace
    fields = ["name", "address", "description", "rating", "image"]
    template_name = "food/place_form_update.html"
    success_url = reverse_lazy("food:place_list")
    login_url = "login"


class PlaceDeleteView(LoginRequiredMixin, DeleteView):
    model = FoodPlace
    template_name = "food/place_confirm_delete.html"
    success_url = reverse_lazy("food:place_list")
    login_url = "login"


class SignUpView(FormView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
