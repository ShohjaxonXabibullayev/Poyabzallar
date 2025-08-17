from django.db import models
from Auth.models import CustomUser


class Category(models.Model):
    category_name = models.CharField(max_length=120)

    def __str__(self):
        return self.category_name

class Poyabzallar(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=100)
    size = models.PositiveIntegerField()
    desc = models.TextField()
    image = models.ImageField(upload_to='poyabzallar-media/', blank=True, null=True, default='default/poyabzal.png')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    made_country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Comments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Poyabzallar, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return f"{self.user.username} - {self.text[:20]}"

