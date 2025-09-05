from django.urls import path
from .views import *

urlpatterns = [
    path('about/',views.about_view,name="about"),
    
]