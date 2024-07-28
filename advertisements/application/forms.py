from django import forms
from .models import WindowsApplication, AndroidApplication


class AdvertisementFormWindows(forms.ModelForm):
    """Form for creating new advertisements"""

    class Meta:
        model = WindowsApplication
        fields = [
            'name', 'title',
            'short_description', 'full_description',
            'image_application_main', 'image_application_2', 'image_application_3',
            'image_application_4', 'image_application_5',
            'name_file_main', 'file_main',
            'name_file_additional', 'file_additional',
        ]

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control bg-dark text-light btn-outline-primary'}
            ),
            'title': forms.TextInput(
                attrs={'class': 'form-control bg-dark text-light btn-outline-primary'}
            ),
            'short_description': forms.Textarea(
                attrs={'class': 'form-control bg-dark text-light btn-outline-primary'}
            ),
            'full_description': forms.Textarea(
                attrs={'class': 'form-control bg-dark text-light btn-outline-primary'}
            ),
            'image_application_main': forms.FileInput(
                attrs={'class': 'form-control bg-dark text-primary btn-outline-primary'}
            ),
            'image_application_2': forms.FileInput(
                attrs={'class': 'form-control bg-dark text-primary btn-outline-primary'}
            ),
            'image_application_3': forms.FileInput(
                attrs={'class': 'form-control bg-dark text-primary btn-outline-primary'}
            ),
            'image_application_4': forms.FileInput(
                attrs={'class': 'form-control bg-dark text-primary btn-outline-primary'}
            ),
            'image_application_5': forms.FileInput(
                attrs={'class': 'form-control bg-dark text-primary btn-outline-primary'}
            ),
            'name_file_main': forms.TextInput(
                attrs={'class': 'form-control bg-dark text-light btn-outline-primary'}
            ),
            'file_main': forms.FileInput(
                attrs={'class': 'form-control bg-dark text-primary btn-outline-primary'}
            ),
            'name_file_additional': forms.TextInput(
                attrs={'class': 'form-control bg-dark text-light btn-outline-primary'}
            ),
            'file_additional': forms.FileInput(attrs={'class': 'form-control bg-dark text-primary btn-outline-primary'}
            ),
        }

    def clean_title(self):
        """Validate that the title is not empty and does not start with a question mark"""
        name = self.cleaned_data.get('name')
        title = self.cleaned_data.get('title')

        if name.startswith('?'):
            raise forms.ValidationError("Title cannot start with a question mark")

        if title.startswith('?'):
            raise forms.ValidationError("Title cannot start with a question mark")

        return name, title


class AdvertisementFormAndroid(forms.ModelForm):
    """Form for creating new advertisements"""

    class Meta:
        model = AndroidApplication
        fields = [
            'name', 'title',
            'short_description', 'full_description',
            'image_application_main', 'image_application_2', 'image_application_3',
            'image_application_4', 'image_application_5',
            'name_file_main', 'file_main',
            'name_file_additional', 'file_additional',
        ]

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control bg-dark text-light btn-outline-primary'}
            ),
            'title': forms.TextInput(
                attrs={'class': 'form-control bg-dark text-light btn-outline-primary'}
            ),
            'short_description': forms.Textarea(
                attrs={'class': 'form-control bg-dark text-light btn-outline-primary'}
            ),
            'full_description': forms.Textarea(
                attrs={'class': 'form-control bg-dark text-light btn-outline-primary'}
            ),
            'image_application_main': forms.FileInput(
                attrs={'class': 'form-control bg-dark text-primary btn-outline-primary'}
            ),
            'image_application_2': forms.FileInput(
                attrs={'class': 'form-control bg-dark text-primary btn-outline-primary'}
            ),
            'image_application_3': forms.FileInput(
                attrs={'class': 'form-control bg-dark text-primary btn-outline-primary'}
            ),
            'image_application_4': forms.FileInput(
                attrs={'class': 'form-control bg-dark text-primary btn-outline-primary'}
            ),
            'image_application_5': forms.FileInput(
                attrs={'class': 'form-control bg-dark text-primary btn-outline-primary'}
            ),
            'name_file_main': forms.TextInput(
                attrs={'class': 'form-control bg-dark text-light btn-outline-primary'}
            ),
            'file_main': forms.FileInput(
                attrs={'class': 'form-control bg-dark text-primary btn-outline-primary'}
            ),
            'name_file_additional': forms.TextInput(
                attrs={'class': 'form-control bg-dark text-light btn-outline-primary'}
            ),
            'file_additional': forms.FileInput(attrs={'class': 'form-control bg-dark text-primary btn-outline-primary'}
            ),
        }

    def clean_title(self):
        """Validate that the title is not empty and does not start with a question mark"""
        name = self.cleaned_data.get('name')
        title = self.cleaned_data.get('title')

        if name.startswith('?'):
            raise forms.ValidationError("Title cannot start with a question mark")

        if title.startswith('?'):
            raise forms.ValidationError("Title cannot start with a question mark")

        return name, title
