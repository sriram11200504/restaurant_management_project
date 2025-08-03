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
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('api/products/', include('products.urls')),
    path('api/orders/', include('orders.urls')),
]
import requests
from django.shortcuts import render
def home(request):
    """
    Renders the homepage and fetches menu data from our API.
    """
    menu_data = []
    try:
        response = requests.get('http://127.0.0.1:8000/api/products/menu/')
        if response.status_code == 200:
            menu_data = response.json()
        else:
            print(f"Error fetching menu: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to API: {e}")
    return render(request, 'home/menu.html', {'menu_items': menu_data})
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Restaurant Menu</title>
    <script src="[https://cdn.tailwindcss.com](https://cdn.tailwindcss.com)"></script>
    <style>
        @import url('[https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap](https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap)');
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f3f4f6;
        }
    </style>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="container mx-auto p-8 bg-white rounded-xl shadow-lg max-w-4xl">
        <h1 class="text-4xl font-extrabold text-center text-gray-900 mb-8">Restaurant Menu</h1>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {% if menu_items %}
                {% for item in menu_items %}
                    <div class="bg-gray-50 rounded-lg p-6 shadow-sm border border-gray-200 hover:shadow-md transition-shadow duration-300">
                        <h2 class="text-2xl font-bold text-gray-800 mb-2">{{ item.name }}</h2>
                        <p class="text-gray-600 mb-4">{{ item.description }}</p>
                        <div class="flex items-center justify-between">
                            <span class="text-3xl font-extrabold text-blue-600">${{ item.price }}</span>
                        </div>
                    </div>
                {% endfor %}
            {% else %}
                <p class="col-span-full text-center text-gray-500 text-lg">Menu not available. Please try again later.</p>
            {% endif %}
        </div>
    </div>
</body>
</html>