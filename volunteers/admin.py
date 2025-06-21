from django.contrib import admin
from volunteers.models import Volunteer

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'joined_at')
    search_fields = ('full_name', 'email', 'phone')
    ordering = ('-joined_at',)
