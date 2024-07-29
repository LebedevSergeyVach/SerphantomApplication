""" Views the list """

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.db.models import Count

from django.contrib.auth.models import User


class WebViews(object):
    """Web views for the app."""

    def welcome(request):
        """ Return the welcome """
        return render(
            request, 'welcome.html'
        )

    def not_found(request):
        """ Return the not_found """
        return render(
            request, '404.html'
        )
