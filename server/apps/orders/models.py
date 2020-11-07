from apps.products.models import Product
from django.db import models
from apps.core.models import AbstractBaseModel
from apps.users.models import User
from apps.markets.models import Market

ORDER_STATUS = (
    (1, 'Confirmado'),
    (2, 'A caminho'),
    (3, 'Entregue')
)


class ShoppingCart(AbstractBaseModel):
    price = models.FloatField(default=0.0)
    amount = models.IntegerField(default=0)
    session_id = models.CharField(max_length=255, blank=True)
    customer = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Order(AbstractBaseModel):
    number = models.CharField(max_length=30)
    status = models.PositiveSmallIntegerField(choices=ORDER_STATUS)
    total = models.FloatField(default=0.0)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)


class OrderItem(AbstractBaseModel):
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
