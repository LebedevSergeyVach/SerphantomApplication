from django.contrib import admin
from .models import Advertisement


# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    """Advertisement Admin"""
    list_display = [
        'id', 'show_user'
    ]

    list_filter = [
        'created_at', 'updated_at'
    ]


admin.site.register(Advertisement, AdvertisementAdmin)
