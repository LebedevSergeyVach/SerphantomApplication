""" Forms for wiews POSt add application """

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    """Custom user creation form."""

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control form-control-lg bg-dark text-light btn-outline-primary",
                "placeholder": "Введите email"
            }
        )
    )

    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg bg-dark text-light btn-outline-primary",
                "placeholder": "Введите номер телефона (необезательно)"
            }
        )
    )

    def __init__(self, *args, **kwargs):
        """Create a new"""
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = \
            'form-control form-control-lg bg-dark text-light btn-outline-primary'
        self.fields['username'].widget.attrs['placeholder'] = \
            'Введите username'
        self.fields['email'].widget.attrs['class'] = \
            'form-control form-control-lg bg-dark text-light btn-outline-primary'
        self.fields['email'].widget.attrs['placeholder'] = \
            'Введите почту'
        self.fields['phone_number'].widget.attrs['class'] = \
            'form-control form-control-lg bg-dark text-light btn-outline-primary'
        self.fields['phone_number'].widget.attrs['placeholder'] = \
            'Введите номер телефона'
        self.fields['password1'].widget.attrs['class'] = \
            'form-control form-control-lg bg-dark text-light btn-outline-primary'
        self.fields['password1'].widget.attrs['placeholder'] = \
            'Введите пароль'
        self.fields['password2'].widget.attrs['class'] = \
            'form-control form-control-lg bg-dark text-light btn-outline-primary'
        self.fields['password2'].widget.attrs['placeholder'] = \
            'Подтвердите пароль'

    class Meta:
        """ Metaclass for the UserCreationForm. """
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]
