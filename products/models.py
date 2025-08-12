from django.db import models
from restaurant_management.models import Restaurant

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=150)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item_name)
class MenuItem(models.Model):
    restaurant=models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='menu_items'
    )
    name=models.CharField(max_length=100)
    description=models.TextField(
        blank=True,
        null=True
    )
    price=models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    is_available=models.BooleanField(
        default=True
    )
    image=models.ImageField(
        upload_to='menu_items/',
        blank=True,
        null=True
    )
    created_at=models.DateTimeField(
        auto_now_add=True
    )
    updated_at=models.DateTimeField(
        auto_now=True
    )

    class Meta:
         unique_together=('restaurant','name')
         ordering=['name']


    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"