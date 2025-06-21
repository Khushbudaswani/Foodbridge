from django import forms
from donations.models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'phone', 'location', 'food_description']
        widgets = {
            'food_description': forms.Textarea(attrs={'rows':4}),
        }
