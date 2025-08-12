from django.db import models
class Restaurant(models.Model):
    name=models.CharField(max_length=255)
    owner_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=20,blank=True)
    address=models.TextField()
opening_hours=models.JSONField(
    default=dict,
    blank=True,
    null=True
)
created_at=models.DateTimeField(auto_now_add=True)
class Meta:
    verbose_name='Restaurant'
    verbose_name_plural='Restaurants'
    ordering=['name']
def __str__(self):
    return self.name