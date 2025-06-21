from django import forms
from pages.models import DonateFood, Volunteer, ContactMessage

class DonateFoodForm(forms.ModelForm):
    class Meta:
        model = DonateFood
        fields = '__all__'

class JoinTeamForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
