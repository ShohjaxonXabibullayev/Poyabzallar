from django.db import models
from products.models import Poyabzallar
from Auth.models import CustomUser


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'paid'),
        ('shipped', 'shipped'),
        ('canceled', 'canceled')
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return self.status

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Poyabzallar, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.product.name

    @property
    def total_price(self):
        return self.product.price * self.amount
