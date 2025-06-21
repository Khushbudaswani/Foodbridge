from django.db import models

class Donation(models.Model):
    name = models.CharField(max_length=100, help_text="Name of donor or business")
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    food_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    fulfilled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.location} ({'Fulfilled' if self.fulfilled else 'Pending'})"

