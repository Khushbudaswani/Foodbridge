"""
Defines the database model for food donations.

This module contains the Donation model, which stores information about
individual food donations, including donor details and donation status.
"""
from django.core.validators import RegexValidator
from django.db import models


class Donation(models.Model):
    """
    Model representing a food donation entry.
    """
    name = models.CharField(max_length=100, help_text="Name of donor or business")
    phone = models.CharField(max_length=20, validators=[RegexValidator(regex=r'^\d{10,15}$', message='Phone number must be 10–15 digits only')])
    location = models.CharField(max_length=200, validators=[RegexValidator(regex=r'^[A-Za-z\s]+$',message='City name must contain only letters and spaces')])
    food_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    fulfilled = models.BooleanField(default=False)

    def __str__(self):
        """
        String representation of the Donation object.
        Shows donor's name, location, and fulfillment status.
        """
        return f"{self.name} - {self.location} ({'Fulfilled' if self.fulfilled else 'Pending'})"

