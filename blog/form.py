from django import forms
from .models import Blog

class Blog_form(forms.ModelForm):
    
    class Meta:
        model= Blog
        fields= [
            'title',
            'image',
            'body',
        ]