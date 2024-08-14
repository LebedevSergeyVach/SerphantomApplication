""" Views the list """

from datetime import datetime

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .forms import UserRegistrationForm

from .device import get_info_divace, get_info_user

from colorama import Fore, Style, init


init()


# Create your views here.


class WebView(object):
    """View class for auth pages"""

    def login_view(request):
        """View function for login page"""
        get_info_user(request)
        device = get_info_divace(request)

        if device == 'mobile':
            no_account = 'Или зарегистрируйтесь!'
            err = 'Вы не зарегистрировались или неверно ввели данные'
        else:
            no_account = 'Нет аккаунта? Зарегистрируйтесь!'
            err = 'Вы не зарегистрировались или неверно ввели данные от аккаунта'

        name_site = 'Вход в аккаунт'

        button_login = 'Войти в аккаунт'
        button_register = 'Зарегистрироваться'

        usr = 'Username'
        passw = 'Password'

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
                'err': '',
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
            f'{Fore.GREEN}Пользователь вошел в аккаунт: '
            f'{Fore.CYAN}[{now.strftime("%Y-%m-%d %H:%M:%S")}]{Style.RESET_ALL}\n'
            f'{Fore.YELLOW}Username and password: '
            f'{Fore.CYAN}{username} {password}{Style.RESET_ALL}\n'
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
        get_info_user(request)
        divace = get_info_divace(request)

        if divace == 'mobile':
            information = 'Необходимо для скачивания программ и приложений'
        else:
            information = 'Необходимо для скачивания программ и приложений на сайте'

        name_site = 'Регистрация аккаунта'

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
                    f'{Fore.GREEN}Пользователь зарегистрировался: '
                    f'{Fore.CYAN}[{now.strftime("%Y-%m-%d %H:%M:%S")}]{Style.RESET_ALL}\n'
                    f'{Fore.YELLOW}Username and password: '
                    f'{Fore.CYAN}{user} {request.POST["password1"]}{Style.RESET_ALL}\n'
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
        print(
            f'{Fore.GREEN}Пользователь вышел из аккаунта: '
            f'{Fore.CYAN}[{now.strftime("%Y-%m-%d %H:%M:%S")}]{Style.RESET_ALL}\n'
        )

        return redirect(
            reverse('welcome')
        )

    @login_required(login_url=reverse_lazy('login'))
    def profile_view(request):
        """View function for profile page"""
        return render(
            request, 'user/profile.html'
        )
