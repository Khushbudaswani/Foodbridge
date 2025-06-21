from django.shortcuts import render
from volunteers.forms import VolunteerForm
from django.core.mail import send_mail
from django.conf import settings

def join_team(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            volunteer = form.save()
            # Notify admin
            send_mail(
                subject='New Volunteer Joined',
                message=f"Name: {volunteer.full_name}\nEmail: {volunteer.email}\nPhone: {volunteer.phone}\nMotivation: {volunteer.motivation}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['daswanikhushbu10@gmail.com'],  # Replace
                fail_silently=True,
            )
            return render(request, 'volunteers/join_team.html', {'form': VolunteerForm(), 'success': True})
    else:
        form = VolunteerForm()
    return render(request, 'volunteers/join_team.html', {'form': form})