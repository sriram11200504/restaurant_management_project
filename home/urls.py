from django.urls import path
from .views import *

urlpatterns = [
    path('about/',views.about_view,name="about"),
    path('our_story/',views.our_story_view,name="our_story"),
    path('reservation/',views.reservations_view,name="reservation"),
    path('feedback_form/',views.feedback_form_view,name="feedback"),
    path('menu/',views.menu_page_view,name="menu_page"),
    path('contact',views.contact_view,name="contact")
]