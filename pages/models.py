from django.db import models


# Model to store information about food donations
class DonateFood(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    food_type = models.CharField(max_length=200)
    quantity = models.CharField(max_length=100)
    pickup_address = models.TextField()
    date = models.DateField(auto_now_add=True) # Date when the food donation was cr

    def __str__(self):
        """Returns a string representation showing the donor's name and food type."""
        return f"{self.name} - {self.food_type}"

# Model to store volunteer information
class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        """Returns the volunteer's name as a string."""
# Model to store messages sent through the contact form
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string showing the sender's name."""
        return f"Message from {self.name}"
