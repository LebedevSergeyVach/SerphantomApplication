""" Views the list """

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.db.models import Count

from django.contrib.auth.models import User

from .models import WindowsApplication, AndroidApplication
from .forms import AdvertisementFormWindows, AdvertisementFormAndroid

import advertisements


class WebViews(object):
    """ Web views for the app """

    def index_windows(request):
        """ Returns the list of windows application """
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
        """ Returns the application for windows """
        advertisement = WindowsApplication.objects.get(pk=pk)

        context = {
            'advertisement': advertisement
        }

        return render(
            request, 'application_windows/application.html', context=context
        )

    def index_android(request):
        """ Returns the list of android application """
        name = request.GET.get('query')

        if name:
            advertisements = AndroidApplication.objects.filter(
                name__icontains=name.strip()
            )
        else:
            advertisements = AndroidApplication.objects.all()

        context = {
            'advertisements': advertisements,
            'title': name
        }

        return render(
            request, 'application_android/index.html', context=context
        )

    def application_android(request, pk):
        """ Returns the application for adndroid """
        advertisement = AndroidApplication.objects.get(pk=pk)

        context = {
            'advertisement': advertisement
        }

        return render(
            request, 'application_android/application.html', context=context
        )

    @login_required(login_url=reverse_lazy('welcome'))
    def add_windows_post(request):
        """ Returns the add application for windows """
        redirect_url = reverse('404')

        if request.user.username in advertisements.secrets.users or request.user.is_superuser:

            if request.method == "POST":
                form = AdvertisementFormWindows(request.POST, request.FILES)

                if form.is_valid():
                    advertisement = form.save(commit=False)
                    advertisement.user = request.user
                    advertisement.save()

                    return redirect(reverse("index-windows"))

            else:
                form = AdvertisementFormWindows()

            context = {'form': form}

        else:
            return redirect(redirect_url)

        return render(
            request, 'application_windows/add-application.html', context=context
        )

    @login_required(login_url=reverse_lazy('welcome'))
    def add_android_post(request):
        """ Returns the add application for android """
        redirect_url = reverse('404')

        if request.user.username in advertisements.secrets.users or request.user.is_superuser:

            if request.method == "POST":
                form = AdvertisementFormAndroid(request.POST, request.FILES)

                if form.is_valid():
                    advertisement = form.save(commit=False)
                    advertisement.user = request.user
                    advertisement.save()

                    return redirect(reverse("index-android"))

            else:
                form = AdvertisementFormAndroid()

            context = {'form': form}

        else:
            return redirect(redirect_url)

        return render(
            request, 'application_android/add-application.html', context=context
        )
