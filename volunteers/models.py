from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class Volunteer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator(message="Enter a valid email address")])
    phone = models.CharField(max_length=20,validators=[RegexValidator(regex=r'^\d{10,15}$',message='Phone number must be 10–15 digits only.')])
    motivation = models.TextField(blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
