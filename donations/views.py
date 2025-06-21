from django.shortcuts import render
from donations.forms import DonationForm
from django.core.mail import send_mail
from django.conf import settings
def donate_food(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'donations/donate_food.html', {'form': DonationForm(), 'success': True})
    else:
        form = DonationForm()
    return render(request, 'donations/donate_food.html', {'form': form})
def donate_food(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save()
            # Send email to site admin
            send_mail(
                subject='New Food Donation Received',
                message=f"Name: {donation.name}\nPhone: {donation.phone}\nLocation: {donation.location}\nFood: {donation.food_description}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['daswanikhushbu10@gmail.com'],  # Replace with your email
                fail_silently=True,
            )
            return render(request, 'donations/donate_food.html', {'form': DonationForm(), 'success': True})
    else:
        form = DonationForm()
    return render(request, 'donations/donate_food.html', {'form': form})