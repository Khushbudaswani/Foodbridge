from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'phone', 'fulfilled', 'created_at')
    list_filter = ('fulfilled', 'created_at')
    search_fields = ('name', 'location', 'phone')
    ordering = ('-created_at',)
