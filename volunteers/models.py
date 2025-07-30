from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class Volunteer(models.Model):
    """
    Model representing a volunteer who wants to join the team.

    Fields:
    - full_name: The full name of the volunteer.
    - email: The email address (validated).
    - phone: The phone number (validated for 10–15 digits).
    - motivation: An optional field where the volunteer can share their motivation.
    - joined_at: Timestamp automatically set when the record is created.
    """
    full_name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator(message="Enter a valid email address")])
    phone = models.CharField(max_length=20,validators=[RegexValidator(regex=r'^\d{10,15}$',message='Phone number must be 10–15 digits only.')])
    motivation = models.TextField(blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name # Display volunteer name in admin panel and shell
