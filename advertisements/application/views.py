""" Views the list """

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.db.models import Count

from django.contrib.auth.models import User

from .models import WindowsApplication, AndroidApplication
from .forms import AdvertisementFormWindows, AdvertisementFormAndroid

from .device import get_info_user

import advertisements


class WebViews(object):
    """ Web views for the app """

    @login_required(login_url=reverse_lazy('login'))
    def index_windows(request):
        """ Returns the list of windows application """
        get_info_user(request)

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

    @login_required(login_url=reverse_lazy('login'))
    def application_windows(request, pk):
        """ Returns the application for windows """
        get_info_user(request)

        redirect_url = reverse('index-windows')

        name = request.GET.get('query')
        # advertisement = WindowsApplication.objects.get(pk=pk)
        advertisement = get_object_or_404(WindowsApplication, pk=pk)

        views_key = f'views_{advertisement.pk}'
        if views_key not in request.session:
            advertisement.number_views += 1
            advertisement.save()
            request.session[views_key] = True

        verified = 'Файл проверен администратором сайта Serphantom -  ✅'
        not_verified = 'Файл не проверен администратором сайта Serphantom - ❌'

        confirmation_deletion = 'Подтверждение удаления программы!'
        deleted = 'Удалить программу'

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

        if request.method == 'POST':
            if 'delete' in request.POST:
                advertisement.delete()
                return redirect(redirect_url)

            if 'verified True' in request.POST:
                advertisement.verified = True
                advertisement.updated_date()
                advertisement.save()

            if 'verified False' in request.POST:
                advertisement.verified = False
                advertisement.updated_date()
                advertisement.save()

            if 'thanks' in request.POST:
                thanks_key = f'thanks_{advertisement.pk}'
                if thanks_key not in request.session:
                    advertisement.number_thanks += 1
                    advertisement.save()
                    request.session[thanks_key] = True

            if 'reset' in request.POST:
                advertisement.number_views = 0
                advertisement.number_thanks = 0
                advertisement.save()

                if not request.user.is_superuser:
                    request.session.flush()

        context = {
            'advertisement': advertisement,
            'meta': meta,
            'verified': verified,
            'not_verified': not_verified,
            'title': name,
            'confirmation_deletion': confirmation_deletion,
            'deleted': deleted,
        }

        return render(
            request, 'application_general/application.html', context=context
        )

    @login_required(login_url=reverse_lazy('login'))
    def index_android(request):
        get_info_user(request)

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

    @login_required(login_url=reverse_lazy('login'))
    def application_android(request, pk):
        get_info_user(request)

        """ Returns the application for adndroid """
        redirect_url = reverse('index-android')

        name = request.GET.get('query')
        advertisement = AndroidApplication.objects.get(pk=pk)

        views_key = f'views_{advertisement.pk}'
        if views_key not in request.session:
            advertisement.number_views += 1
            advertisement.save()
            request.session[views_key] = True

        verified = 'Файл проверен администратором сайта Serphantom -  ✅'
        not_verified = 'Файл не проверен администратором сайта Serphantom - ❌'

        confirmation_deletion = 'Подтверждение удаления приложения!'
        deleted = 'Удалить приложение'

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

        if request.method == 'POST':
            if 'delete' in request.POST:
                advertisement.delete()
                return redirect(redirect_url)

            if 'verified True' in request.POST:
                advertisement.verified = True
                advertisement.updated_date()
                advertisement.save()

            if 'verified False' in request.POST:
                advertisement.verified = False
                advertisement.updated_date()
                advertisement.save()

            if 'thanks' in request.POST:
                thanks_key = f'thanks_{advertisement.pk}'
                if thanks_key not in request.session:
                    advertisement.number_thanks += 1
                    advertisement.save()
                    request.session[thanks_key] = True

            if 'reset' in request.POST:
                advertisement.number_views = 0
                advertisement.number_thanks = 0
                advertisement.save()

                if not request.user.is_superuser:
                    request.session.flush()

        context = {
            'advertisement': advertisement,
            'meta': meta,
            'verified': verified,
            'not_verified': not_verified,
            'title': name,
            'confirmation_deletion': confirmation_deletion,
            'deleted': deleted,
        }

        return render(
            request, 'application_general/application.html', context=context
        )

    @login_required(login_url=reverse_lazy('welcome'))
    def add_windows_post(request):
        """ Returns the add application for windows """
        get_info_user(request)

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
        get_info_user(request)

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
