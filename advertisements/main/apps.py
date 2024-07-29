""" Apps for application in settings.py """

from django.apps import AppConfig


class MainConfig(AppConfig):
    """ Config for the application that will be used to interact with """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
