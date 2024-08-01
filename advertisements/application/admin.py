""" Admin interface for accessing """

from django.contrib import admin
from .models import WindowsApplication, AndroidApplication


# Register your models here.

class WindowsApplicationAdmin(admin.ModelAdmin):
    """ WindowsApplication Admin """

    list_display = [
        'id', 'name',
        'show_image_application_main', 'show_image_application_2', 'show_image_application_3',
        'name_file_main', 'file_main',
        'created_date',
    ]

    list_filter = [
        'created_at', 'updated_at'
    ]

    fieldsets = (
        ('Добавить приложение Windows', {
            'fields': ('user', 'name', 'title',
                       'short_description', 'full_description',
                       'image_application_main',
                       'name_file_main', 'file_main')
        }),

        ('Дополнительные медиа данные', {
            'fields': ('image_application_2', 'image_application_3',
                       'image_application_4', 'image_application_5',
                       'name_file_additional', 'file_additional'),

            'classes': ['collapse']
        })
    )


class AndroidApplicationAdmin(admin.ModelAdmin):
    """ AndroidApplication Admin """

    list_display = [
        'id', 'name',
        'show_image_application_main', 'show_image_application_2', 'show_image_application_3',
        'name_file_main', 'file_main',
        'created_date',
    ]

    list_filter = [
        'created_at', 'updated_at'
    ]

    fieldsets = (
        ('Добавить приложение Windows', {
            'fields': ('user', 'name', 'title',
                       'short_description', 'full_description',
                       'image_application_main',
                       'name_file_main', 'file_main')
        }),

        ('Дополнительные медиа данные', {
            'fields': ('image_application_2', 'image_application_3',
                       'image_application_4', 'image_application_5',
                       'name_file_additional', 'file_additional'),

            'classes': ['collapse']
        })
    )


""" Registration methods """
admin.site.register(WindowsApplication, WindowsApplicationAdmin)
admin.site.register(AndroidApplication, AndroidApplicationAdmin)
