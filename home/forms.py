from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,required=False,help_text="your name")
    email=forms.EmailField(required=True,help_text="your email")
    subject=forms.CharField(required=False,max_length=200,help_text="your subject")
    message=forms.CharField(width=forms.Textarea,required=True,help_text="your message")
    