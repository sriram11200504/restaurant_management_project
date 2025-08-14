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
def contact_view(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data["message"]

            email_subject=f"contact form submission:{subject}"
            email_body= f"name: {name if name else 'Ananimous'}\n" \
                        f"email: {email}\n" \
                        f"subject: {subject}\n" \
                        f"message: {message}\n" \
            try:
                send_mail(
                    email_subject,
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.RECIPEINT_EMAIL],
                    fail_silently=False,
                )
                return render(request,'home/contact_form.html',{
                    'form':ContactForm(),
                    'success message': 'your message has sent successfully',
                    'restaurant_name':settings.RESTAURANT_NAME
                })
            except Exception as e:
                print(f"error sending email: {e}")
                return render(request,'home/contact_form.html',{
                    'form':ContactForm(),
                    'error_message':'there is a error in sending message',
                    'restaurant_name': settings.RESTAURANT_NAME
                })
        else:
            return render(request,'home/contact_form.html',{
                'form':ContactForm(),
                'restaurant_name':settings.RESTAURANT_NAME
            })
    else:
        form=ContactForm()
        return render(request,'home/contact_form.html',{
            'form':form,
            'restaurant_name':settings.RESTAURANT_NAME
        })

    return render(request,'home/menu.html',context)