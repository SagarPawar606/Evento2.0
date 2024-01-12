from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')


def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            messages.success(request, f'Welcome, {name} to Evento')
            # authenticate and login user
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('account-home')
    return render(request, 'accounts/register.html', {'form':form})

