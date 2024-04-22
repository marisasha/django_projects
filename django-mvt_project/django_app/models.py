from django.contrib.auth.models import User
from django.db import models 
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(
        verbose_name="Автор",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        max_length=300,
        to=User,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    name =  models.TextField(
        verbose_name = 'Имя',
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null = True,
        default = None,
        max_length=100
    )
    surname = models.TextField(
        verbose_name = 'Фамилия',
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null = True,
        default = None,
        max_length=100
    )
    
    description = models.TextField(
        verbose_name = 'Краткая информация',
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null = True,
        default = None,
        max_length=100
    )

    avatar = models.ImageField(
        verbose_name="Аватарка",
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="images/Noneavatar.jpg",
        upload_to="images/",
    )

    class Meta:
        app_label = "auth"
        ordering = ("-user",)

    def __str__(self):
        return f"<Profile {self.user.username} ({self.id})/>"



@receiver(post_save, sender=User)
def profile_create(sender, instance: User, created: bool, **kwargs):
    profile = Profile.objects.get_or_create(user=instance)



class Friends(models.Model):
    
    user = models.OneToOneField(
        verbose_name="Пользователь",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=True,
        default="",
        max_length=300,
        to=User,
        on_delete=models.CASCADE,
        related_name = "user_friends"
    )

    friends = models.ManyToManyField(
        verbose_name = 'Друзья',
        max_length=300,
        to=User,
        related_name = "friends"
    )
    class Meta:
        app_label = "auth"
        verbose_name = "Друзья"
        verbose_name_plural = "Друзья"

    def __str__(self):
        return f"<Friends ({self.id}) />"


@receiver(post_save, sender=User)
def profile_create(sender, instance: User, created: bool, **kwargs):
    Friends.objects.get_or_create(user=instance)
    

class ApplicationFriends(models.Model):
    
    user = models.OneToOneField(
        verbose_name="Пользователь",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=True,
        default="",
        max_length=300,
        to=User,
        on_delete=models.CASCADE,
        related_name = "user_application"
    )

    application = models.ManyToManyField(
        verbose_name = 'Запросы ',
        max_length=300,
        unique=False,
        to=User,
        related_name = "application"
    )
    class Meta:
        app_label = "auth"
        verbose_name = "Запросы в друзья"
        verbose_name_plural = "Запросы в друзья"

    def __str__(self):
        return f"<Friends ({self.id}) />"
    

@receiver(post_save, sender=User)
def profile_create(sender, instance: User, created: bool, **kwargs):
    ApplicationFriends.objects.get_or_create(user=instance)


class Room(models.Model):
    name = models.CharField(
        verbose_name="Наименование",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=255,
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
        max_length=300,
    )
    users = models.ManyToManyField(
        verbose_name="Участники чата",
        max_length=50,
        to = User
    )

    class Meta:
        app_label = "auth"
        ordering = ("name",)
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return f"<Group {self.name}({self.id}) />"
    

class Message(models.Model):
    user = models.ForeignKey(
        verbose_name="Автор",
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
    room = models.ForeignKey(
        verbose_name="Комната",
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        to=Room,
        on_delete=models.CASCADE,
    )
    content = models.TextField(
        verbose_name="Текст сообщения",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )
    date_added = models.DateTimeField(
        verbose_name="дата и время добавления",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=timezone.now,
        max_length=300,
    )

    class Meta:
        app_label = "auth"
        ordering = ("-date_added", "-room")
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return f"<Message {self.room.name} {self.user.username} {self.content[:30]} ({self.id})/>"
    
class News(models.Model):
    user = models.ForeignKey(
        verbose_name="Автор",
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

    content = models.CharField(
        verbose_name="Текст поста",
        db_index=False,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=True,
        default="",
    )
    image = models.ImageField(
        verbose_name="Картинка",
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="",
        upload_to="news_images/",
    )
    date_added = models.DateTimeField(
        verbose_name="дата и время добавления",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=timezone.now,
        max_length=300,
    )

    class Meta:
        app_label = "auth"
        ordering = ("-date_added","user")
        verbose_name = "Пост пользователей"
        verbose_name_plural = "Пост пользователей"

    def __str__(self) -> str:
        return f"<News {self.user.username} {self.content[:30]} ({self.id})/>"
