from django.db import models
from apps.markets.models import Market
from apps.core.models import AbstractBaseModel


class Category(AbstractBaseModel):
    name = models.CharField(max_length=80, blank=False)


class Product(AbstractBaseModel):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    price = models.FloatField(default=0.0)
    amount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
