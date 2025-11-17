from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class FoodPlace(models.Model):
    CATEGORY_CHOICES = [
        ('restaurant', 'Restaurant'),
        ('bakery', 'Bakery'),
        ('market', 'Market'),
        ('producer', 'Artisan Producer'),
        ('coffee', 'Coffee Shop'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='restaurant')
    image = models.ImageField(upload_to='places/', blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='places')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('food:place_detail', args=[str(self.id)])
