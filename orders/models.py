from django.db import models
from django.contrib.auth.models import User
from products.models import MenuItem

ORDER_STATUS_CHOICES=(
    ('PENDING','pending'),
    ('PREPARING','preparing'),
    ('DELIVERED','delivered'),
    ('CANCELLED','cancelled'),
)

class Order(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    total_amount=models.DecimalField(max_digits=8,decimal_places=2,default=0.00)
    status=models.CharField(max_length=20,choices=ORDER_STATUS_CHOICES,default='PENDING')
    created_At=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"order #{self.id} by {self.customer.username}"
class Feedback(models.Model):
    customer_name=models.CharField(max_length=100,blank=True,null=True)
    customer_email=models.EmailField(blank=True,null=True)
    comments=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['created_at']
    def __str__(self):
        if self.customer_name:
            return f"Feedback from {self.customer_name} ({self.created_at.strftime('%Y-%m-%d %H:%M')})
        elif self.customer_email:
            return f"Feedback from {self.customer_email} ({self.created_at.strftime('%Y-%m-%d %H-%M')})
        return f"Anonymous Feedback({self.created_at.strftime('%Y-%m-%d %H-%M')})