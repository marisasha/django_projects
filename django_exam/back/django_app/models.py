from django.contrib.auth.models import User
from django.db import models 
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(
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
    name =  models.CharField(
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null = True,
        default = None,
        max_length=100
    )
    surname = models.CharField(
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null = True,
        default = None,
        max_length=100
    )
    

@receiver(post_save, sender=User)
def profile_create(sender, instance: User, created: bool, **kwargs):
    profile = Profile.objects.get_or_create(user=instance)

class Post(models.Model):
    user = models.ForeignKey(
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
        db_index=False,
        primary_key=False,
        unique=True,
        editable=True,
        blank=True,
        null=True,
        default="",
        max_length = 1000
        
    )
    image = models.ImageField(
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        upload_to="static",
    )
    date_added = models.DateTimeField(
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=timezone.now,
        max_length=300,
    )

    
    
class Comment(models.Model):
    user = models.ForeignKey(
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
    post_for_comment = models.ForeignKey(
        db_index=True,
        primary_key=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=100,
        to=Post,
        on_delete=models.CASCADE,
    )
    content = models.TextField(
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )
    date_added = models.DateTimeField (
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default=timezone.now,
        max_length=300,
    )

