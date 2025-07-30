from django import forms

from donations.models import Donation


class DonationForm(forms.ModelForm):
    """
    Form to collect food donation details from users.
    """
    class Meta:
        model = Donation
        fields = ['name', 'phone', 'location', 'food_description']
        widgets = {
            'food_description': forms.Textarea(attrs={'rows':4}),
        }
