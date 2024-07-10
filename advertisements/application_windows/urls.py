from django.urls import path
from .views import WebViews


urlpatterns = [
    path('', WebViews.not_found, name='main-index'),

    path('Windows', WebViews.index_windows, name='index-windows'),
    path('Android', WebViews.index_android, name='index-android'),

    path('add-windows-post', WebViews.add_windows_post, name='add-windows-post'),
    path('add-android-post', WebViews.add_android_post, name='add-android-post'),

    path('404', WebViews.not_found, name='404')
]
