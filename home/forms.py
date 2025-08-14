from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,required=False)
    email=forms.EmailField(required=True)
    subject=forms.CharField(required=False,max_length=200)
    message=forms.CharField(width=forms.Textarea,required=True)
    