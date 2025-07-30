from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from volunteers.forms import VolunteerForm


def join_team(request):
    """
    View to handle volunteer form submission.
    
    - On GET: Displays an empty form.
    - On POST: Validates and saves form data, sends an email notification, and shows a success message.
    """
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            volunteer = form.save()
            # Email notification to admin about new volunteer
            send_mail(
                subject='New Volunteer Joined',
                message=f"Name: {volunteer.full_name}\nEmail: {volunteer.email}\nPhone: {volunteer.phone}\nMotivation: {volunteer.motivation}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['daswanikhushbu10@gmail.com'],  # Replace
                fail_silently=True,# Set to False in production to catch email errors
            )
            # Render the form again with a success message
            return render(request, 'volunteers/join_team.html', {'form': VolunteerForm(), 'success': True})
    else:
        form = VolunteerForm()
    return render(request, 'volunteers/join_team.html', {'form': form})