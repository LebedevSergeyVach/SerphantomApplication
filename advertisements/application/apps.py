""" Apps for application in settings.py """

from django.apps import AppConfig


class AppAdvertisementsConfig(AppConfig):
    """ Config for the application that will be used to interact with """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'application'
    verbose_name = 'Приложения Windows databases'
