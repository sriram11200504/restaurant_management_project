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
    <title>HomeFoods-taste it</title>
    <script src="[https://cdn.tailwindcss.com](https://cdn.tailwindcss.com)"></script>
    <style>
        @import url('[https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap](https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap)');
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f3f4f6;
        }
        h1{
            color:red;
        }
        button_container{
            text-align: center;
            margin-top:40px;
            margin-bottom:40px;
        }
        order_button{
            background-color:#ff6347;
            color:white;
            padding:15px 30px;
            border:2px solid orange;
        }
        
    </style>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="container mx-auto p-8 bg-white rounded-xl shadow-lg max-w-4xl">
   <a href="#"><img src="https://img.freepik.com/premium-vector/restaurant-logo-design-template_79169-56.jpg?w=2000" alt="log"/></a>
    <div>
       <h1>Welcome to the HomeFoods Restaurant where you''ll find the flavor of your home</h1>
    </div>
    
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
    <div class="container mx-auto p-8 bg-white rounded-xl shadow-lg max-w-4xl">
        <h2>contact us</h2>
        <div class="flex flex-col md:flew-row gap-6">
            <div class="md:w-1/2 p-4 bg-gray-50 rounded-lg shadow-sm border border-gray-200">
               <p class="text-lg font-semibold text-gray-800" style="color:red;">Our Location</p>
               <address class="noy-italic text-gray-500 mt-2">
               123 main street<br>
               new york,CA 90210<br>
               united states 
               </address>
               <p class="text-gray-600 mt-4">
               Phone:<a href="tel:+91 7981265232" class="text-blue-600 hover:underline">(555) 123-4567</a>
               </p>
               
            </div>
            <div class="md:w-1/2 rounded-lg overflow-hidden border border-gray-200">
              <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3153.242777134375!2d-122.41941568468165!3d37.7749294797585!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80858064d42e616f%3A0x1d542d99d3d3a0c7!2sSan%20Fransisco%2C%20CA!5e0!3m2!1sen!2sus!4v1625078400000!5m2!1sen!2sus" width="100%" height="300" allowfullscreen"" loading="lazy"></iframe>
            </div>
            <div class="button_container" style="color:red;">
              <a href="#" class="order_button">Order Now</a>
            </div>
        </div>
    </div>
    <footer bg-color="palewhite">
    &copy;<span id="Current-Year"></span>{{restaurant_name}}. ALL RIGHTS RESERVED.
    <a href="policypage.html">terms of service</a>
    </footer>
    <script> 
    document.getElementById("Current-Year").innerHTML=new Date().getFullYear();
    </script>
</body>

</html>