from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.db.models import Count

from django.contrib.auth.models import User

from .models import WindowsApplication


class WebViews(object):
    """Web views for the app."""

    def welcome(request):
        return render(
            request, 'welcome.html'
        )

    def index_windows(request):
        name = request.GET.get('query')

        if name:
            advertisements = WindowsApplication.objects.filter(
                name__icontains=name.strip()
            )
        else:
            advertisements = WindowsApplication.objects.all()

        context = {
            'advertisements': advertisements,
            'title': name
        }

        return render(
            request, 'application_windows/index.html', context=context
        )

    def application_windows(request, pk):
        advertisement = WindowsApplication.objects.get(pk=pk)

        context = {
            'advertisement': advertisement
        }

        return render(
            request, 'application_windows/application.html', context=context
        )

    def index_android(request):
        return render(
            request, 'application_android/index.html'
        )

    def add_windows_post(request):
        return render(
            request, 'application_windows/add-windows-post.html'
        )

    def add_android_post(request):
        return render(
            request, 'application_android/add-android-post.html'
        )

    def not_found(request):
        return render(
            request, '404.html'
        )
