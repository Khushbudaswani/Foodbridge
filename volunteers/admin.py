"""
Admin configuration for the Volunteer model in the volunteers app.

This file customizes how the Volunteer model appears in the Django admin interface,
including display columns, search fields, and ordering.
"""
from django.contrib import admin
from volunteers.models import Volunteer

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    """
    Admin customization for the Volunteer model.
    
    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        search_fields (tuple): Fields that can be searched in the admin.
        ordering (tuple): Default ordering of volunteer entries.
    """
    list_display = ('full_name', 'email', 'phone', 'joined_at')
    search_fields = ('full_name', 'email', 'phone')
    ordering = ('-joined_at',)
