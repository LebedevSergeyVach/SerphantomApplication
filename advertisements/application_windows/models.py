from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.


User = get_user_model()


class Advertisement(models.Model):
    """ Advertisement model """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )

    name = models.CharField(
        verbose_name="Название",
        max_length=30,
    )

    title = models.CharField(
        verbose_name="Заголовок",
        max_length=100,
    )

    short_description = models.TextField(
        verbose_name="Кратное описание",
        max_length=5000,
    )

    full_description = models.TextField(
        verbose_name="Полное описание",
        max_length=50000,
    )

    image_application_main = models.ImageField(
        verbose_name="Изображение",
        upload_to="advertisements/image",
    )

    image_application_2 = models.ImageField(
        verbose_name="Дополнительное изображение",
        upload_to="advertisements/image",
        null=True,
        blank=True,
    )

    image_application_3 = models.ImageField(
        verbose_name="Дополнительное изображение",
        upload_to="advertisements/image",
        null=True,
        blank=True,
    )

    image_application_4 = models.ImageField(
        verbose_name="Дополнительное изображение",
        upload_to="advertisements/image",
        null=True,
        blank=True,
    )

    image_application_5 = models.ImageField(
        verbose_name="Дополнительное изображение",
        upload_to="advertisements/image",
        null=True,
        blank=True,
    )

    file_main = models.FileField(
        verbose_name="Главный файл",
        upload_to="advertisements/files",
    )

    file_main = models.FileField(
        verbose_name="Дополнительный файл",
        upload_to="advertisements/files",
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description="Дата создания")
    def created_date(self):
        """Show the date of the creation"""
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")

            return format_html(
                '<span style="color: blue; font-weight: bold;">Сегодня в {}</span>', created_time
            )

        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description="Дата изменения")
    def updated_date(self):
        """Show the date of the update"""
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime("%H:%M:%S")

            return format_html(
                '<span style="color: green; font-weight: bold">Сегодня в {}</span>', created_time
            )

        return self.updated_at.strftime(f"%d.%m.%Y в %H:%M:%S")

    @admin.display(description="Пользователь")
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

    def __str__(self):
        """String representation"""
        return f'id = {self.id} title = {self.name} price = {self.title}'

    def get_absolute_url(self):
        """Get absolute URL for this user from the database"""
        return reverse(
            'advertisement', kwargs={'pk': self.pk}
        )

    class Meta:
        """Meta options"""
        db_table = 'advertisement'
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
