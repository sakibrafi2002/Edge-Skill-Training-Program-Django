from django import forms
from typing import Any
from .models import Book

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('Email must be from google.com domain.')
        return email
    
    
    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'publication_date', 'author', 'price']

        # Custom validation for the price field
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be a positive number.")
        return price