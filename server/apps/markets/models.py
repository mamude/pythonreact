from django.db import models
from apps.core.models import AbstractBaseModel


class CategoryBusiness(AbstractBaseModel):
    name = models.CharField(max_length=80, blank=False)


class Market(AbstractBaseModel):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    url = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=21)
    rating = models.FloatField(default=0.0)
    distance = models.CharField(max_length=20)
    delivery_time = models.CharField(max_length=20)
    delivery_tax = models.FloatField(default=0.0)
    category_business = models.ForeignKey(
        CategoryBusiness, on_delete=models.CASCADE)
