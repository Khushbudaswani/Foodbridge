from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    """
    Admin interface for the Donation model.
    Allows list display, filtering, and search capabilities in the admin panel.
    """
    list_display = ('name', 'location', 'phone', 'fulfilled', 'created_at') # Fields to display in list view
    list_filter = ('fulfilled', 'created_at') # Filters in right sidebar
    search_fields = ('name', 'location', 'phone') # Search functionality
    ordering = ('-created_at',)  # Default ordering (newest first)
