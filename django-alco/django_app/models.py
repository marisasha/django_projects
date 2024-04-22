from django.db import models
from django.utils import timezone

class AlcoQR(models.Model):
    title = models.CharField(
        verbose_name="Название",
        db_index=True,
        editable=True,
        unique = False,
        blank = True,
        null = False,
        default="",
        max_length=300
    )
    images = models.ImageField(
        verbose_name="Картинка",
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        upload_to="images",
    )
    description = models.TextField(
        verbose_name="Описание",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )
    date = models.DateTimeField(
        verbose_name="дата и время создания",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=timezone.now,
        max_length=300,
    )

