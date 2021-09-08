from django.db import models
from django.urls import reverse


class Products(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-list')