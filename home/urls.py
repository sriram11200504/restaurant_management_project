from django.urls import path
from .views import *

urlpatterns = [
    path('about/',views.about_view,name="about"),
    path('our_story/',views.ourstory_view)
]