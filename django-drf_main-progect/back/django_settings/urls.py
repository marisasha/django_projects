from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path,include,re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("django_app.urls")),
    path("api-auth/", include("rest_framework.urls")),
    
]
