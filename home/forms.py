from django import forms
from .models import newslettersubscriber

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,required=False,help_text="your name")
    email=forms.EmailField(required=True,help_text="your email")
    subject=forms.CharField(required=False,max_length=200,help_text="your subject")
    message=forms.CharField(width=forms.Textarea,required=True,help_text="your message")
class newsletterform(forms.ModelForm):
    class Meta:
        model=newslettersubscriber
        fields=['email']
    