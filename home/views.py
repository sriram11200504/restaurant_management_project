import requests
from django.shortcuts import render
from django.conf import settings

def home(request):
    menu_data=[]
    try:
        response=requests.get('http://127.0.0.1:8000/api/products/menu-items/')

        if response.status_code=200:
            menu_data=response.json()
        else:
            print(f"error fetching menu : {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"failed to connect to API: {e}")

    context={
        'menu-item' = menu_data,
        'restaurant_name'=settings.RESTAURANT_NAME
    }
    return render(request,'home/menu.html',context)
