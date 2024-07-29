""" Urls the specified resource with the specified name """

from django.urls import path
from .views import WebViews


urlpatterns = [
    path('', WebViews.welcome, name='welcome'),
    path('404', WebViews.not_found, name='404')
]
