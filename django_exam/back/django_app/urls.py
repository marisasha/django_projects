from django.contrib import admin
from django.urls import path
from django_app import views

urlpatterns = [
    path("",view=views.home),
]
