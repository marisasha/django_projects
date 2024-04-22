from django.contrib import admin
from django_app import models

# Register your models here.
admin.site.register(models.Profile)
admin.site.register(models.Friends)
admin.site.register(models.ApplicationFriends)
admin.site.register(models.Room)
admin.site.register(models.News)
