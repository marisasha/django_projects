from django.shortcuts import render
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User


def home(request):
    return render( 
        request=request,
        template_name="index.html",
        context={
            "hi":"hi"
        }
    )