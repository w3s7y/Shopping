from django.db import models
from django.contrib.auth.models import User


CURRENCY_CHOICES = (
    ('£', 'GBP'),
    ('$', 'USD'),
)


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True)
    price = models.FloatField()
    price_unit = models.CharField(max_length=1, choices=CURRENCY_CHOICES)
    barcode = models.BigIntegerField(blank=True)


class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    website = models.URLField(blank=True)


class List(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class ItemListMap(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)


class Offer(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.FloatField()
    price_unit = models.CharField(max_length=1, choices=CURRENCY_CHOICES)
    end_date = models.DateField(blank=True)


class Favorite(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
