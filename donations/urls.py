"""
URL configuration for the donations app.

This module defines the URL patterns for routing HTTP requests
to the appropriate view functions within the donations app.
"""

from django.urls import path

from donations import views

# URL patterns for the donations app
urlpatterns = [
    # Route for the food donation form page
    path('', views.donate_food, name='donate_food'),
    
]
