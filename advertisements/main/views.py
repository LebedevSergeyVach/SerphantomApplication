from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.db.models import Count

from django.contrib.auth.models import User


class WebViews(object):
    """Web views for the app."""

    def welcome(request):
        return render(
            request, 'welcome.html'
        )

    def not_found(request):
        return render(
            request, '404.html'
        )
