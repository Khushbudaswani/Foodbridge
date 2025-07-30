from django import forms

from pages.models import ContactMessage, DonateFood, Volunteer


# Form for food donation, linked to the DonateFood model
class DonateFoodForm(forms.ModelForm):
    """
    Form for users to donate food.

    This form is directly tied to the DonateFood model and includes all fields from it.
    """
    class Meta:
        model = DonateFood # Model used for the form
        fields = '__all__' # Includes all model fields
# Form for users to join as volunteers, linked to the Volunteer model

class JoinTeamForm(forms.ModelForm):
    """
    Form for users to join the volunteering team.

    Maps to the Volunteer model and includes all fields.
    """
    class Meta:
        model = Volunteer
        fields = '__all__'

# Contact form for users to send messages, tied to the ContactMessage model
class ContactForm(forms.ModelForm):
    """
    Form for users to send a contact message.

    Only includes name, email, and message fields from the ContactMessage model.
    """
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
