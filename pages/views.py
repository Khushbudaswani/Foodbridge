from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect


def signup_view(request):
    """
    Handles user registration using a custom version of UserCreationForm
    that removes help texts from form fields.
    
    If the request is POST and form is valid, logs in the user and redirects to home.
    Otherwise, displays form with error messages.
    """
    from django import forms
    from django.contrib.auth.forms import UserCreationForm
    class CustomUserCreationForm(UserCreationForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Remove help text from all fields
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
    """
    Handles user login using Django's built-in AuthenticationForm.
    
    On POST: Validates and logs in user, displays success or failure message.
    On GET: Renders the empty login form.
    """
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
    """
    Logs out the user and redirects to home page on POST request.
    """
    if request.method == 'POST':
        logout(request)
        return redirect('home')
from django.shortcuts import redirect, render

from pages.forms import ContactForm, DonateFoodForm, JoinTeamForm


def home(request):
    """Renders the homepage."""
    return render(request, 'pages/home.html')

def about(request):
    """Renders the about page."""
    return render(request, 'pages/about.html')

def donate_food(request):
    """
    Handles the food donation form submission.
    
    On POST: Validates and saves the form, shows success message.
    On GET: Displays empty form.
    """
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
    """
    Handles the team joining form submission.
    
    On POST: Validates and saves the form, shows success message.
    On GET: Displays empty form.
    """
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
    """Renders the events page."""
    return render(request, 'pages/events.html')

def impact(request):
    return render(request, 'pages/impact.html')

def partners(request):
    return render(request, 'pages/partners.html')

def contact(request):
    """
    Handles the contact form submission.
    
    On POST: Validates the form and sets success flag.
    On GET: Displays empty form.
    """
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
