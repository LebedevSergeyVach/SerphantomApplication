""" Views the list """

from datetime import datetime

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .forms import UserRegistrationForm


# Create your views here.


class WebView(object):
    """View class for auth pages"""

    def login_view(request):
        """View function for login page"""
        name_site = 'Вход в аккаунт'
        no_account = 'Нет аккаунта? Зарегистрируйтесь!'

        button_login = 'Войти в аккаунт'
        button_register = 'Зарегистрироваться'

        usr = 'Username'
        passw = 'Password'

        err = 'Вы не зарегистрировались или неверно вели данные'

        if request.user.is_authenticated:
            return redirect('404')

        redirect_url = reverse('index-windows')

        if request.method == 'GET':
            if request.user.is_authenticated:
                return redirect(redirect_url)

            context = {
                'name_site': name_site,
                'no_account': no_account,
                'button_login': button_login,
                'button_register': button_register,
                'usr': usr,
                'passw': passw,
                'error': '',
            }

            return render(
                request, 'user/login.html', context=context
            )

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request, username=username, password=password,
        )

        # DEBUG
        now = datetime.now()
        print(
            f'# Пользователь вошел в аккаунт: [{now.strftime("%Y-%m-%d %H:%M:%S")}]\n'
            f'Username: {username} Password: {password}'
        )

        if user is not None:
            login(request, user)
            return redirect(redirect_url)

        context = {
            'name_site': name_site,
            'no_account': no_account,
            'button_login': button_login,
            'button_register': button_register,
            'usr': usr,
            'passw': passw,
            'error': err,
        }

        return render(
            request, 'user/login.html', context=context
        )

    def register_view(request):
        """View function for register page"""
        name_site = 'Регистрация аккаунта'
        information = 'Необходимо для скачивания программ и приложений на сайте'

        an_account = 'Есть аккаунта? Войдите!'

        button_login = 'Войти в аккаунт'
        button_register = 'Зарегистрироваться'

        if request.user.is_authenticated:
            return redirect('404')

        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)

            if form.is_valid():
                user = form.save()

                user = authenticate(
                    username=user.username, password=request.POST['password1']
                )

                login(request, user=user)

                # DEBUG
                now = datetime.now()
                print(
                    f'# Пользователь зарегистрировался: [{now.strftime("%Y-%m-%d %H:%M:%S")}]\n'
                    f'Username: {user} Password: {request.POST["password1"]}'
                )

                return redirect(reverse('index-windows'))

        else:
            form = UserRegistrationForm()

        context = {
            'form': form,
            'name_site': name_site,
            'information': information,
            'an_account': an_account,
            'button_login': button_login,
            'button_register': button_register,
        }

        return render(
            request, 'user/register.html', context=context
        )

    @login_required(login_url=reverse_lazy('login'))
    def logout_view(request):
        """View function for logout page"""
        logout(request)

        # DEBUG
        now = datetime.now()
        print(f'# Пользователь вышел из аккаунта: [{now.strftime("%Y-%m-%d %H:%M:%S")}] ')

        return redirect(
            reverse('welcome')
        )

    @login_required(login_url=reverse_lazy('login'))
    def profile_view(request):
        """View function for profile page"""
        return render(
            request, 'user/profile.html'
        )
