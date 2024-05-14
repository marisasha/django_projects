from django.contrib.auth.models import User
from django.db import models 
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(
        verbose_name="Пользователь",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        to=User,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    name =  models.CharField(
        verbose_name = 'Имя',
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null = True,
        default = None,
        max_length=50
    )
    surname = models.CharField(
        verbose_name = 'Фамилия',
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null = True,
        default = None,
        max_length=50
    )

    number = models.CharField(
        verbose_name = "Номер",
        db_index = True,
        primary_key =False,
        editable=True,
        blank=True,
        null = False,
        max_length=12
    )

    avatar = models.ImageField(
        verbose_name="Аватарка",
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="startap_avatars/Noneavatar.jpg",
        upload_to="startap_avatars/",
    )
    data_register = models.DateTimeField(
        verbose_name="Дата и регистрации",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=timezone.now,
    )

    class Meta:
        app_label = "auth"
        ordering = ("-name",)
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return f"<Profile [{self.id}] {self.user.username} />"



@receiver(post_save, sender=User)
def profile_create(sender, instance: User, created: bool, **kwargs):
    profile = Profile.objects.get_or_create(user=instance)


class CategoryStartap(models.Model):
    title = models.CharField(
        verbose_name="Наименование",
        db_index=True,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=40,
    )
    image = models.ImageField(
        verbose_name="Картинка",
        validators=[FileExtensionValidator(["jpg", "png", "jpeg", "bmp"])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        upload_to="startap_category/",
    )
    slug = models.SlugField(  
        verbose_name="Ссылка",
        db_index=True,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=40,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-title",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"<CategoryItem [{self.id}] {self.title}/>"


class Startap(models.Model):
    
    user = models.ForeignKey(
        verbose_name="Автор",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        to=User,
        on_delete=models.CASCADE,
    )
    

    category = models.ForeignKey(
        verbose_name="Категория",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        to=CategoryStartap,
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        verbose_name="Название",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        max_length=100,
    )

    description = models.TextField(
        verbose_name="Описание",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False
    )

    location = models.CharField(
        verbose_name="Местоположение",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        default="",
        null=False,
        max_length=50,
    )

    deposit_amount = models.PositiveIntegerField(
        verbose_name="Сумма вклада",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        default=0,
        null=False
    )

    pdf = models.FileField(
        validators=[FileExtensionValidator(["pdf"])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        upload_to="startap_pdf/",
    )

    image = models.ImageField(
        verbose_name="Аватарка",
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        upload_to="startap_avatars/",
    )

    data = models.DateTimeField(
        verbose_name="Дата и время создания",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=timezone.now,
    )
    is_active = models.BooleanField(
        verbose_name="Активность",
        null=False,
        default=True,
    )
    class Meta:
        app_label = "django_app"
        ordering = ("-title",)
        verbose_name = "Стартап"
        verbose_name_plural = "Стартапы"

    def __str__(self):
        return f"<Startap [{self.id}] {self.title}/>"


class FilesStartap(models.Model):
    
    startap = models.ForeignKey(
        verbose_name="Стартап",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        to=Startap,
        on_delete=models.CASCADE,
    )

    file = models.FileField(
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        upload_to="startap_files/",
    )
    class Meta:
        app_label = "django_app"
        ordering = ("id",)
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

    def __str__(self):
        return f"<FilesStartap [{self.id}]/>"


class LikeStartap(models.Model):
    author = models.ForeignKey(
        verbose_name='Автор',
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        to=User,
        on_delete=models.CASCADE,
    )
    startap = models.ForeignKey(
        verbose_name="Объявление",
        db_index=True,
        primary_key=False,
        editable=True,
        unique=False,
        blank=True,
        null=False,
        default="",
        max_length=100,
        to=Startap,
        on_delete=models.CASCADE,
    )

    class Meta:
        app_label = "django_app"
        ordering = ("-id",)
        verbose_name = "Активнность лайка"
        verbose_name_plural = "Активнность лайка"

    def __str__(self):
        return f"<LikeStartap[{self.id}]({self.author})/>"