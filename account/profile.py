INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'account',
    'home',
    'orders',
    'products', 
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', include('products.urls')),
    path('api/orders/', include('orders.urls'))
]
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

from django.urls import path
urlpatterns = [
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
]


from django.shortcuts import render

from rest_framework import serializers
class MenuItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MenuItemSerializer
class MenuView(APIView):
    """
    A view that returns a hardcoded restaurant menu.
    """
    def get(self, request):
        menu_data = [
            {
                "name": "Grilled Salmon",
                "description": "Fresh salmon fillet with a lemon-dill sauce and roasted asparagus.",
                "price": 24.99
            },
            {
                "name": "Mushroom Risotto",
                "description": "Creamy Arborio rice with wild mushrooms, truffle oil, and parmesan cheese.",
                "price": 18.50
            },
            {
                "name": "Chocolate Lava Cake",
                "description": "Warm chocolate cake with a molten center, served with a scoop of vanilla ice cream.",
                "price": 9.25
            },
        ]
        serializer = MenuItemSerializer(menu_data, many=True)
        return Response(serializer.data)

from django.urls import path
from .views import MenuView

urlpatterns = [
    path('menu/', MenuView.as_view(), name='menu-list'),
]
