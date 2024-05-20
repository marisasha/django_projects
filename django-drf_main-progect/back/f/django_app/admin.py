from django.contrib import admin
from django_app import models

# Register your models here.
admin.site.register(models.Profile)
admin.site.register(models.Startap)
admin.site.register(models.CategoryStartap)
admin.site.register(models.FilesStartap)
admin.site.register(models.LikeStartap)
admin.site.register(models.Commentses)

