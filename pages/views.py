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
