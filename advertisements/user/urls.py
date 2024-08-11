""" Urls the specified resource with the specified name """

from django.urls import path

from .views import WebView

urlpatterns = [
    path('login/', WebView.login_view, name='login'),
    path('logout/', WebView.logout_view, name='logout'),
    path('register/', WebView.register_view, name='register'),
]
