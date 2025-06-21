from django import forms
from volunteers.models import Volunteer

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['full_name', 'email', 'phone', 'motivation']
        widgets = {
            'motivation': forms.Textarea(attrs={'rows':3}),
        }
