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

        description = 'Продукция для Windows'
        name_site = 'Windows application'

        meta = (
            'Serphantom Space - сайт для пользователей Windows и Android. '
            'На данном сайте размещаются программы и приложения для Windows и Android. '
            'Любой пользователь сайта может необходимые ему программы или приложения. '
            
            'Добро пожаловать, дорогой гость! Serphantom Space Windows application. '
            'Programs, applications and products for Windows. Программы, приложения и продукция для Windows. '
        )

        if name:
            advertisements = WindowsApplication.objects.filter(
                name__icontains=name.strip()
            )
        else:
            advertisements = WindowsApplication.objects.all()

        context = {
            'advertisements': advertisements,
            'title': name,
            'description': description,
            'meta': meta,
            'name_site': name_site,
        }

        return render(
            request, 'application_windows/index.html', context=context
        )

    def application_windows(request, pk):
        """ Returns the application for windows """
        redirect_url = reverse('index-windows')

        name = request.GET.get('query')
        advertisement = WindowsApplication.objects.get(pk=pk)

        verified = 'Файл проверен администратором сайта Serphantom -  ✅'
        not_verified = 'Файл не проверен администратором сайта Serphantom - ❌'

        meta = (
            'Сайт для пользователей Windows и Android. '
            'На данном сайте размещаются программы и приложения для Windows и Android. '
            'Любой пользователь сайта может необходимые ему программы или приложения. '
            'Добро пожаловать, дорогой гость! '
        
            'Programs, applications and products for Android. '
            'Программы, приложения и продукция для Android. '
        )

        if name:
            advertisements = WindowsApplication.objects.filter(
                name__icontains=name.strip()
            )
            return redirect(redirect_url)
        else:
            advertisements = WindowsApplication.objects.all()

        context = {
            'advertisement': advertisement,
            'meta': meta,
            'verified': verified,
            'not_verified': not_verified,
            'title': name,
        }

        return render(
            request, 'application_general/application.html', context=context
        )

    def index_android(request):
        """ Returns the list of android application """
        name = request.GET.get('query')

        description = 'Приложения для Android'
        name_site = 'Android application'

        meta = (
            'Serphantom Space - сайт для пользователей Windows и Android. '
            'На данном сайте размещаются программы и приложения для Windows и Android. '
            'Любой пользователь сайта может необходимые ему программы или приложения. '

            'Добро пожаловать, дорогой гость! Serphantom Space Windows application. '
            'Programs, applications and products for Android. Программы, приложения и продукция для Android. '
        )

        if name:
            advertisements = AndroidApplication.objects.filter(
                name__icontains=name.strip()
            )
        else:
            advertisements = AndroidApplication.objects.all()

        context = {
            'advertisements': advertisements,
            'title': name,
            'description': description,
            'meta': meta,
            'name_site': name_site,
        }

        return render(
            request, 'application_android/index.html', context=context
        )

    def application_android(request, pk):
        """ Returns the application for adndroid """
        redirect_url = reverse('index-android')

        name = request.GET.get('query')
        advertisement = AndroidApplication.objects.get(pk=pk)

        verified = 'Файл проверен администратором сайта Serphantom -  ✅'
        not_verified = 'Файл не проверен администратором сайта Serphantom - ❌'

        meta = (
            'Сайт для пользователей Windows и Android. '
            'На данном сайте размещаются программы и приложения для Windows и Android. '
            'Любой пользователь сайта может необходимые ему программы или приложения. '
            'Добро пожаловать, дорогой гость! '

            'Programs, applications and products for Windows. '
            'Программы, приложения и продукция для Windows. '
        )

        if name:
            advertisements = WindowsApplication.objects.filter(
                name__icontains=name.strip()
            )
            return redirect(redirect_url)
        else:
            advertisements = WindowsApplication.objects.all()

        context = {
            'advertisement': advertisement,
            'meta': meta,
            'verified': verified,
            'not_verified': not_verified,
            'title': name,
        }

        return render(
            request, 'application_general/application.html', context=context
        )

    @login_required(login_url=reverse_lazy('welcome'))
    def add_windows_post(request):
        """ Returns the add application for windows """
        redirect_url = reverse('404')

        description = 'Продукция для Windows'
        name_site = 'Add application Windows'

        if request.user.username in advertisements.secrets.users or request.user.is_superuser:

            if request.method == 'POST':
                form = AdvertisementFormWindows(request.POST, request.FILES)

                if form.is_valid():
                    advertisement = form.save(commit=False)
                    advertisement.user = request.user
                    advertisement.save()

                    return redirect(reverse('index-windows'))

            else:
                form = AdvertisementFormWindows()

            context = {
                'form': form,
                'description': description,
                'name_site': name_site,
            }

        else:
            return redirect(redirect_url)

        return render(
            request, 'application_general/add-application.html', context=context
        )

    @login_required(login_url=reverse_lazy('welcome'))
    def add_android_post(request):
        """ Returns the add application for android """
        redirect_url = reverse('404')

        description = 'Приложения для Android'
        name_site = 'Add application Android'

        if request.user.username in advertisements.secrets.users or request.user.is_superuser:

            if request.method == 'POST':
                form = AdvertisementFormAndroid(request.POST, request.FILES)

                if form.is_valid():
                    advertisement = form.save(commit=False)
                    advertisement.user = request.user
                    advertisement.save()

                    return redirect(reverse('index-android'))

            else:
                form = AdvertisementFormAndroid()

            context = {
                'form': form,
                'description': description,
                'name_site': name_site,
            }

        else:
            return redirect(redirect_url)

        return render(
            request, 'application_general/add-application.html', context=context
        )
