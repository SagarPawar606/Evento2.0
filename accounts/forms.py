from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=255, help_text='Enter Organization name if organizer')

    class Meta:
        model = CustomUser
        fields = ("email", "name", "password1", "password2")

    
    

