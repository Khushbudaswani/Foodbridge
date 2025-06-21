from django.db import models

class DonateFood(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    food_type = models.CharField(max_length=200)
    quantity = models.CharField(max_length=100)
    pickup_address = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.food_type}"

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
