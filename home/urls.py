from django.urls import path
from .views import *

urlpatterns = [
    path('about/',views.about_view,name="about"),
    path('our_story/',views.our_story_view,name="our_story"),
    path('reservation/',views.reservations_view,name="reservation"),
    
]