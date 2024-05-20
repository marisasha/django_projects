from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path,include,re_path

def redirect_to_home(request):
    return redirect('/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("django_app.urls")),
    path("api-auth/", include("rest_framework.urls")),
    re_path(r"^.*$", redirect_to_home)
    
]
