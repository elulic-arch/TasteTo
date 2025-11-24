from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    rating = models.IntegerField(blank=True, null=True)  # 1–5 rating
    image = models.ImageField(upload_to="places/", blank=True, null=True)

    def __str__(self):
        return self.name
