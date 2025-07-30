from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from donations.forms import DonationForm


def donate_food(request):
    """
    Handles food donation form submission and email notification.

    - On a POST request:
        - Validates the submitted donation form.
        - Saves the donation data to the database.
        - Sends a notification email to the site admin with donation details.
        - Returns the donation form template with a success message.

    - On a GET request:
        - Renders an empty donation form.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: The rendered donation form page.
    """
    if request.method == 'POST':
        # Populate form with submitted data
        form = DonationForm(request.POST)
        if form.is_valid():
            # Save donation instance to database
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
                fail_silently=True,  # Prevents app from crashing if email fails
            )
            # Re-render the form with a success message
            return render(request, 'donations/donate_food.html', {'form': DonationForm(), 'success': True})
    else:
        # For GET request, show empty form
        form = DonationForm()
    return render(request, 'donations/donate_food.html', {'form': form})