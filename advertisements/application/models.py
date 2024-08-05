""" Models for databae """

from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.


User = get_user_model()


class WindowsApplication(models.Model):
    """ WindowsApplication model """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )

    name = models.CharField(
        verbose_name='Название',
        max_length=30,
    )

    title = models.TextField(
        verbose_name='Заголовок',
        max_length=100,
    )

    short_description = models.TextField(
        verbose_name='Кратное описание',
        max_length=5000,
    )

    full_description = models.TextField(
        verbose_name='Полное описание',
        max_length=50000,
    )

    image_application_main = models.ImageField(
        verbose_name='Изображение',
        upload_to='application_windows/image',
    )

    image_application_2 = models.ImageField(
        verbose_name='Дополнительное изображение',
        upload_to='application_windows/image',
        null=True,
        blank=True,
    )

    image_application_3 = models.ImageField(
        verbose_name='Дополнительное изображение',
        upload_to='application_windows/image',
        null=True,
        blank=True,
    )

    image_application_4 = models.ImageField(
        verbose_name='Дополнительное изображение',
        upload_to='application_windows/image',
        null=True,
        blank=True,
    )

    image_application_5 = models.ImageField(
        verbose_name='Дополнительное изображение',
        upload_to='application_windows/image',
        null=True,
        blank=True,
    )

    file_main = models.FileField(
        verbose_name='Главный файл',
        upload_to='application_windows/files',
    )

    file_additional = models.FileField(
        verbose_name='Дополнительный файл',
        upload_to='application_windows/files',
        null=True,
        blank=True,
    )

    name_file_main = models.CharField(
        verbose_name='Название главного файла',
        max_length=30,
    )

    name_file_additional = models.CharField(
        verbose_name='Название дополнительного файла',
        max_length=30,
        null=True,
        blank=True,
    )

    verified = models.BooleanField(
        verbose_name='Файл проверен администратором сайта',
        default=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        """Show the date of the creation"""
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")

            return format_html(
                '<span style="color: blue; font-weight: bold;">Сегодня в {}</span>', created_time
            )

        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='Дата изменения')
    def updated_date(self):
        """Show the date of the update"""
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime('%H:%M:%S')

            return format_html(
                '<span style="color: green; font-weight: bold">Сегодня в {}</span>', created_time
            )

        return self.updated_at.strftime(f'%d.%m.%Y в %H:%M:%S')

    @admin.display(description='Пользователь')
    def show_user(self):
        """Show the user"""
        if self.user.is_superuser:
            return format_html(
                '<span style="color: red; font-weight: bold;">Администратор</span>'
            )
        else:
            return format_html(
                '<span style="color: blue; font-weight: bold;">{}</span>', self.user.username
            )

    @admin.display(description='Изображение')
    def show_image_application_main(self):
        """Show the image"""
        if self.image_application_main:
            return format_html(
                '<img src={} style="width: 70px; height: 50px">', self.image_application_main.url
            )
        else:
            return format_html(
                '<img src="https://pa1.narvii.com/7435/efabf45acf29e0c694a56ec3871779f6f5434fc7r1-640-360_hq.gif"'
                'style="width: 70px; height: 50px">'
            )

    @admin.display(description='Изображение 2')
    def show_image_application_2(self):
        """Show the image"""
        if self.image_application_2:
            return format_html(
                '<img src={} style="width: 70px; height: 50px">', self.image_application_2.url
            )
        else:
            return format_html(
                '<img src="https://pa1.narvii.com/7435/efabf45acf29e0c694a56ec3871779f6f5434fc7r1-640-360_hq.gif"'
                'style="width: 70px; height: 50px">'
            )

    @admin.display(description='Изображение 3')
    def show_image_application_3(self):
        """Show the image"""
        if self.image_application_3:
            return format_html(
                '<img src={} style="width: 70px; height: 50px">', self.image_application_3.url
            )
        else:
            return format_html(
                '<img src="https://pa1.narvii.com/7435/efabf45acf29e0c694a56ec3871779f6f5434fc7r1-640-360_hq.gif"'
                'style="width: 70px; height: 50px">'
            )

    @admin.display(description='Изображение 4')
    def show_image_application_4(self):
        """Show the image"""
        if self.image_application_4:
            return format_html(
                '<img src={} style="width: 70px; height: 50px">', self.image_application_4.url
            )
        else:
            return format_html(
                '<img src="https://pa1.narvii.com/7435/efabf45acf29e0c694a56ec3871779f6f5434fc7r1-640-360_hq.gif"'
                'style="width: 70px; height: 50px">'
            )

    @admin.display(description='Изображение 5')
    def show_image_application_5(self):
        """Show the image"""
        if self.image_application_5:
            return format_html(
                '<img src={} style="width: 70px; height: 50px">', self.image_application_5.url
            )
        else:
            return format_html(
                '<img src="https://pa1.narvii.com/7435/efabf45acf29e0c694a56ec3871779f6f5434fc7r1-640-360_hq.gif"'
                'style="width: 70px; height: 50px">'
            )

    @admin.display(description='Файл проверен')
    def show_verified(self):
        """Show the verified status"""
        if self.verified:
            return format_html(
                '<span style="color: blue; font-weight: bold;">🍏</span>'
            )
        else:
            return format_html(
                '<span style="color: red; font-weight: bold;">🍎</span>'
            )

    def __str__(self):
        """String representation"""
        return f'id = {self.id} title = {self.name} price = {self.title}'

    def get_absolute_url(self):
        """Get absolute URL for this user from the database"""
        return reverse(
            'application-windows', kwargs={'pk': self.pk}
        )

    class Meta:
        """Meta options"""
        db_table = 'WindowsApplication'
        verbose_name = 'WindowsApplication'
        verbose_name_plural = 'WindowsApplication'


class AndroidApplication(models.Model):
    """ AndroidApplication model """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )

    name = models.CharField(
        verbose_name='Название',
        max_length=30,
    )

    title = models.TextField(
        verbose_name='Заголовок',
        max_length=100,
    )

    short_description = models.TextField(
        verbose_name='Кратное описание',
        max_length=5000,
    )

    full_description = models.TextField(
        verbose_name='Полное описание',
        max_length=50000,
    )

    image_application_main = models.ImageField(
        verbose_name='Изображение',
        upload_to='application_windows/image',
    )

    image_application_2 = models.ImageField(
        verbose_name='Дополнительное изображение',
        upload_to='application_windows/image',
        null=True,
        blank=True,
    )

    image_application_3 = models.ImageField(
        verbose_name='Дополнительное изображение',
        upload_to='application_windows/image',
        null=True,
        blank=True,
    )

    image_application_4 = models.ImageField(
        verbose_name='Дополнительное изображение',
        upload_to='application_windows/image',
        null=True,
        blank=True,
    )

    image_application_5 = models.ImageField(
        verbose_name='Дополнительное изображение',
        upload_to='application_windows/image',
        null=True,
        blank=True,
    )

    file_main = models.FileField(
        verbose_name='Главный файл',
        upload_to='application_windows/files',
    )

    file_additional = models.FileField(
        verbose_name='Дополнительный файл',
        upload_to='application_windows/files',
        null=True,
        blank=True,
    )

    name_file_main = models.CharField(
        verbose_name='Название главного файла',
        max_length=30,
    )

    name_file_additional = models.CharField(
        verbose_name='Название дополнительного файла',
        max_length=30,
        null=True,
        blank=True,
    )

    verified = models.BooleanField(
        verbose_name='Файл проверен администратором сайта',
        default=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        """Show the date of the creation"""
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")

            return format_html(
                '<span style="color: blue; font-weight: bold;">Сегодня в {}</span>', created_time
            )

        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='Дата изменения')
    def updated_date(self):
        """Show the date of the update"""
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime('%H:%M:%S')

            return format_html(
                '<span style="color: green; font-weight: bold">Сегодня в {}</span>', created_time
            )

        return self.updated_at.strftime(f'%d.%m.%Y в %H:%M:%S')

    @admin.display(description='Пользователь')
    def show_user(self):
        """Show the user"""
        if self.user.is_superuser:
            return format_html(
                '<span style="color: red; font-weight: bold;">Администратор</span>'
            )
        else:
            return format_html(
                '<span style="color: blue; font-weight: bold;">{}</span>', self.user.username
            )

    @admin.display(description='Изображение')
    def show_image_application_main(self):
        """Show the image"""
        if self.image_application_main:
            return format_html(
                '<img src={} style="width: 70px; height: 50px">', self.image_application_main.url
            )
        else:
            return format_html(
                '<img src="https://pa1.narvii.com/7435/efabf45acf29e0c694a56ec3871779f6f5434fc7r1-640-360_hq.gif"'
                'style="width: 70px; height: 50px">'
            )

    @admin.display(description='Изображение 2')
    def show_image_application_2(self):
        """Show the image"""
        if self.image_application_2:
            return format_html(
                '<img src={} style="width: 70px; height: 50px">', self.image_application_2.url
            )
        else:
            return format_html(
                '<img src="https://pa1.narvii.com/7435/efabf45acf29e0c694a56ec3871779f6f5434fc7r1-640-360_hq.gif"'
                'style="width: 70px; height: 50px">'
            )

    @admin.display(description='Изображение 3')
    def show_image_application_3(self):
        """Show the image"""
        if self.image_application_3:
            return format_html(
                '<img src={} style="width: 70px; height: 50px">', self.image_application_3.url
            )
        else:
            return format_html(
                '<img src="https://pa1.narvii.com/7435/efabf45acf29e0c694a56ec3871779f6f5434fc7r1-640-360_hq.gif"'
                'style="width: 70px; height: 50px">'
            )

    @admin.display(description='Изображение 4')
    def show_image_application_4(self):
        """Show the image"""
        if self.image_application_4:
            return format_html(
                '<img src={} style="width: 70px; height: 50px">', self.image_application_4.url
            )
        else:
            return format_html(
                '<img src="https://pa1.narvii.com/7435/efabf45acf29e0c694a56ec3871779f6f5434fc7r1-640-360_hq.gif"'
                'style="width: 70px; height: 50px">'
            )

    @admin.display(description='Изображение 5')
    def show_image_application_5(self):
        """Show the image"""
        if self.image_application_5:
            return format_html(
                '<img src={} style="width: 70px; height: 50px">', self.image_application_5.url
            )
        else:
            return format_html(
                '<img src="https://pa1.narvii.com/7435/efabf45acf29e0c694a56ec3871779f6f5434fc7r1-640-360_hq.gif"'
                'style="width: 70px; height: 50px">'
            )

    @admin.display(description='Файл проверен')
    def show_verified(self):
        """Show the verified status"""
        if self.verified:
            return format_html(
                '<span style="color: blue; font-weight: bold;">🍏</span>'
            )
        else:
            return format_html(
                '<span style="color: red; font-weight: bold;">🍎</span>'
            )

    def __str__(self):
        """String representation"""
        return f'id = {self.id} title = {self.name} price = {self.title}'

    def get_absolute_url(self):
        """Get absolute URL for this user from the database"""
        return reverse(
            'application-android', kwargs={'pk': self.pk}
        )

    class Meta:
        """Meta options"""
        db_table = 'AndroidApplication'
        verbose_name = 'AndroidApplication'
        verbose_name_plural = 'AndroidApplication'
