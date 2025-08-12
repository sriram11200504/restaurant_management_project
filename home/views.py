import requests
from django.shortcuts import render
from django.conf import settings
def home(request):
    menu_data=[]
    try:
        response=requests.get('http://127.0.0.1:8000/api/products/menu-items/')
        if response.status_code==200:
            menu_data=response.json()
        else:
            print(f"error fetching menu: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"failed to connect to API: {e}")
    
    context={
        'menu_items': menu_data,
        'restaurant_name': settings.RESTAURANT_NAME
    }
    return render(request,'home/menu.html',context)
def about_view(request):
    context={
        'restaurant_name': settings.RESTAURANT_NAME
    }
    return render(request,'home/about.html',context)
def reservations_view(request):
    context={
        'restaurant_name': settings.RESTAURANT_NAME
    }
    return render(request,'home/reservation.html',context)
def feedback_form_view(request):
    context={
        'restaurant_name': settings.RESTAURANT_NAME
    }
    return render(request,'home/feedback_form.html',context)
def menu_page_view(request):
    search_query=request.GET.get('q','')
    if search_query:
        menu_items=MenuItem.objects.filter(name__icontains=search_query).order_by('name')
    else:
        menu_items=MenuItem.objects.all().order_by('name')
    context={
        'restaurant_name': settings.RESTAURANT_NAME,
        'menu_items':menu_items,
        'search_query':search_query
    }
    return render(request,'home/menu.html',context)