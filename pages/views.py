from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect

def signup_view(request):
    from django.contrib.auth.forms import UserCreationForm
    from django import forms
    class CustomUserCreationForm(UserCreationForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.help_text = ''
    message = ''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            message = 'Please correct the errors below.'
    else:
        form = CustomUserCreationForm()
    return render(request, 'pages/signup.html', {'form': form, 'message': message})

def login_view(request):
    from django.contrib.auth.forms import AuthenticationForm
    message = ''
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            message = 'Login successful!'
            return render(request, 'pages/login.html', {'form': form, 'message': message, 'success': True})
        else:
            message = 'Invalid username or password.'
            return render(request, 'pages/login.html', {'form': form, 'message': message, 'success': False})
    else:
        form = AuthenticationForm()
    return render(request, 'pages/login.html', {'form': form, 'message': message})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
from django.shortcuts import render, redirect
from pages.forms import DonateFoodForm, JoinTeamForm, ContactForm

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def donate_food(request):
    success = False
    if request.method == 'POST':
        form = DonateFoodForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = DonateFoodForm()
    return render(request, 'pages/donate_food.html', {'form': form, 'success': success})

def join_team(request):
    success = False
    if request.method == 'POST':
        form = JoinTeamForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = JoinTeamForm()
    return render(request, 'pages/join_team.html', {'form': form, 'success': success})

def events(request):
    return render(request, 'pages/events.html')

def impact(request):
    return render(request, 'pages/impact.html')

def partners(request):
    return render(request, 'pages/partners.html')

def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save or send email here
            success = True
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'success': success})

def gallery(request):
    return render(request, 'pages/gallery.html')
