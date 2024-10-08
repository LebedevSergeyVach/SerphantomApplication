""" Urls the specified resource with the specified name """

from django.urls import path
from .views import WebViews


urlpatterns = [
    path('windows', WebViews.index_windows, name='index-windows'),
    path('android', WebViews.index_android, name='index-android'),

    path('product/<int:pk>', WebViews.application_windows, name='application-windows'),
    path('application/<int:pk>', WebViews.application_android, name='application-android'),

    path('add-windows-post', WebViews.add_windows_post, name='add-windows-post'),
    path('add-android-post', WebViews.add_android_post, name='add-android-post'),
]
