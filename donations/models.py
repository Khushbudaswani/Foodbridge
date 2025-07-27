from django.db import models
from django.core.validators import RegexValidator

class Donation(models.Model):
    name = models.CharField(max_length=100, help_text="Name of donor or business")
    phone = models.CharField(max_length=20, validators=[RegexValidator(regex=r'^\d{10,15}$', message='Phone number must be 10–15 digits only')])
    location = models.CharField(max_length=200, validators=[RegexValidator(regex=r'^[A-Za-z\s]+$',message='City name must contain only letters and spaces')])
    food_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    fulfilled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.location} ({'Fulfilled' if self.fulfilled else 'Pending'})"

