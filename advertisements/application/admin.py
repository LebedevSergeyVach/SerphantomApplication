""" Admin interface for accessing """

from django.contrib import admin
from django.contrib import messages

from .models import WindowsApplication, AndroidApplication


# Register your models here.

class WindowsApplicationAdmin(admin.ModelAdmin):
    """ WindowsApplication Admin """

    list_display = [
        'id', 'name',
        'show_image_application_main', 'show_image_application_2', 'show_image_application_3',
        'name_file_main',
        'created_date',
        'show_verified',
    ]

    list_filter = [
        'created_at', 'updated_at', 'verified',
    ]

    actions = [
        'make_verified_as_true', 'make_verified_as_false',
    ]

    fieldsets = (
        ('Добавить приложение Windows', {
            'fields': ('user', 'name', 'title',
                       'short_description', 'full_description',
                       'image_application_main',
                       'name_file_main', 'file_main', 'verified',)
        }),

        ('Дополнительные медиа данные', {
            'fields': ('image_application_2', 'image_application_3',
                       'image_application_4', 'image_application_5',
                       'name_file_additional', 'file_additional'),

            'classes': ['collapse']
        })
    )

    @admin.action(description='Файл проверен администратором сайта')
    def make_verified_as_true(self, request, queryset):
        """Make the possibility of bargaining"""
        updated = queryset.update(verified=True)

        if updated:
            self.message_user(request, f'{updated} Файл проверен администратором сайта.', messages.SUCCESS)
        else:
            self.message_user(request, 'Действие не было выполнено.', messages.WARNING)

    @admin.action(description='Файл не проверен администратором сайта')
    def make_verified_as_false(self, request, queryset):
        """Remove the possibility of bargaining"""
        updated = queryset.update(verified=False)

        if updated:
            self.message_user(request, f'{updated} Файл не проверен администратором сайта.', messages.SUCCESS)
        else:
            self.message_user(request, 'Действие не было выполнено.', messages.WARNING)

    # Данный говнокодище нахилдится в разработке...
    @admin.action(description='Make name application')
    def make_name_application(self, request, queryset):
        """Изменяет название выбранных приложений на 'New Application Name'"""
        updated = queryset.update(name='New Application Name')
        if updated:
            self.message_user(request, f'{updated} приложений было переименовано.', messages.SUCCESS)
        else:
            self.message_user(request, 'Ни одно приложение не было переименовано.', messages.WARNING)


class AndroidApplicationAdmin(admin.ModelAdmin):
    """ AndroidApplication Admin """

    list_display = [
        'id', 'name',
        'show_image_application_main', 'show_image_application_2', 'show_image_application_3',
        'name_file_main',
        'created_date',
        'show_verified',
    ]

    list_filter = [
        'created_at', 'updated_at', 'verified',
    ]

    actions = [
        'make_verified_as_true', 'make_verified_as_false',
    ]

    fieldsets = (
        ('Добавить приложение Windows', {
            'fields': ('user', 'name', 'title',
                       'short_description', 'full_description',
                       'image_application_main',
                       'name_file_main', 'file_main', 'verified',)
        }),

        ('Дополнительные медиа данные', {
            'fields': ('image_application_2', 'image_application_3',
                       'image_application_4', 'image_application_5',
                       'name_file_additional', 'file_additional'),

            'classes': ['collapse']
        })
    )

    @admin.action(description='Файл проверен администратором сайта')
    def make_verified_as_true(self, request, queryset):
        """Make the possibility of bargaining"""
        updated = queryset.update(verified=True)

        if updated:
            self.message_user(request, f'{updated} Файл проверен администратором сайта.', messages.SUCCESS)
        else:
            self.message_user(request, 'Действие не было выполнено.', messages.WARNING)

    @admin.action(description='Файл не проверен администратором сайта')
    def make_verified_as_false(self, request, queryset):
        """Remove the possibility of bargaining"""
        updated = queryset.update(verified=False)

        if updated:
            self.message_user(request, f'{updated} Файл не проверен администратором сайта.', messages.SUCCESS)
        else:
            self.message_user(request, 'Действие не было выполнено.', messages.WARNING)


""" Registration methods """
admin.site.register(WindowsApplication, WindowsApplicationAdmin)
admin.site.register(AndroidApplication, AndroidApplicationAdmin)
