from django.db import models
# Create your models here.
from Poyabzallar.settings import AUTH_USER_MODEL
from products.models import Poyabzallar

User = AUTH_USER_MODEL

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Poyabzallar, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.PositiveIntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

    @property
    def total_price(self):
        return self.product.price * self.amount

