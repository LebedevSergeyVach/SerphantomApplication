from django.contrib import admin
from .models import WindowsApplication, AndroidApplication


# Register your models here.

class WindowsApplicationAdmin(admin.ModelAdmin):
    """ WindowsApplication Admin """

    list_display = [
        'id', 'name', 'show_image_application_main', 'file_main'
    ]

    list_filter = [
        'created_at', 'updated_at'
    ]

    fieldsets = (
        ('Добавить приложение Windows', {
            'fields': ('user', 'name', 'title',
                       'short_description', 'full_description',
                       'image_application_main', 'file_main')
        }),

        ('Дополнительные медиа данные', {
            'fields': ('image_application_2', 'image_application_3',
                       'image_application_4', 'image_application_5',
                       'file_additional'),

            'classes': ['collapse']
        })
    )


class AndroidApplicationAdmin(admin.ModelAdmin):
    """ AndroidApplication Admin """

    list_display = [
        'id', 'name', 'show_image_application_main', 'file_main'
    ]

    list_filter = [
        'created_at', 'updated_at'
    ]

    fieldsets = (
        ('Добавить приложение Windows', {
            'fields': ('user', 'name', 'title',
                       'short_description', 'full_description',
                       'image_application_main', 'file_main')
        }),

        ('Дополнительные медиа данные', {
            'fields': ('image_application_2', 'image_application_3',
                       'image_application_4', 'image_application_5',
                       'file_additional'),

            'classes': ['collapse']
        })
    )


admin.site.register(WindowsApplication, WindowsApplicationAdmin)
admin.site.register(AndroidApplication, AndroidApplicationAdmin)
