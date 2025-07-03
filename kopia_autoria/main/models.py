from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class CarAd(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand.name} {self.model} ({self.year})"

class AdView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carad = models.ForeignKey(CarAd, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'carad', 'timestamp']

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    carad = models.ForeignKey(CarAd, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'carad']
