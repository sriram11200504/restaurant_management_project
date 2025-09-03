from django.db import models

# Create your models here.
class newslettersubscriber(models.Model):
    email=models.EmailField(unique=True,help_text="Enter you email to subscribe")
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email