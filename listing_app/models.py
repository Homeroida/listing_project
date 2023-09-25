from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')


class Status(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Location(models.Model):
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city}, {self.country}"


class Listing(models.Model):
    photos = models.ManyToManyField(Photo)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    view_counter = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
