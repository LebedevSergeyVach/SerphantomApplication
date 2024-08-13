""" Views the list """

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.db.models import Count

from django.contrib.auth.models import User

from .device import get_info_user


class WebViews(object):
    """Web views for the app."""

    def welcome(request):
        """ Return the welcome """
        get_info_user(request)

        name_site = 'Serphantom'
        title = 'SERPHANROM SPACE'
        display = 'Добро пожаловать!'
        text = 'На данном сайте можете скачать интересующие Вас приложения.'

        button_Windows = 'Windows'
        button_Android = 'Android'
        button_GitHub = 'GitHub'
        button_admin = 'Admin'
        button_login = 'Вход'
        button_register = 'Регистрация'

        context = {
            'name_site': name_site,
            'title': title,
            'display': display,
            'text': text,
            'button_Windows': button_Windows,
            'button_Android': button_Android,
            'button_GitHub': button_GitHub,
            'button_admin': button_admin,
            'button_login': button_login,
            'button_register': button_register,
        }

        return render(
            request, 'main/welcome.html', context=context
        )

    def not_found(request):
        """ Return the not_found """
        get_info_user(request)

        name_site = 'Страница не найдена'
        title = '404'
        display_opps = 'Page not found.'
        display_not_found = 'Добро пожаловать!'
        text = 'The page you’re looking for doesn’t exist.'

        button_go_home = 'Go Home'
        button_admin = 'Admin'

        context = {
            'name_site': name_site,
            'title': title,
            'display_opps': display_opps,
            'display_not_found': display_not_found,
            'text': text,
            'button_go_home': button_go_home,
            'button_admin': button_admin,
        }

        return render(
            request, 'main/404.html', context=context
        )
