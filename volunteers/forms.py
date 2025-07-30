from django import forms
from volunteers.models import Volunteer

class VolunteerForm(forms.ModelForm):
    """
    Form for users to submit their interest in volunteering.

    This form is based on the Volunteer model and includes fields such as:
    - full_name: Name of the volunteer.
    - email: Contact email.
    - phone: Contact number.
    - motivation: Reason for joining the volunteering team.
    """
    class Meta:
        model = Volunteer  # The model this form is associated with
        fields = ['full_name', 'email', 'phone', 'motivation'] # Fields to include in the form

        widgets = {
            'motivation': forms.Textarea(attrs={'rows':3}),
        }
