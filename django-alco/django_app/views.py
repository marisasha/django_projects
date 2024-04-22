from datetime import datetime
import os
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.cache import caches
from django_app import models
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
import re
import qrcode



def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        username = str(request.POST["username"])
        password = str(request.POST["password"])
        password_accept = str(request.POST["password_accept"])
        if password != password_accept:
            return render(request, "register.html", context={"error": "Пароли не совпадают!"})
        usr = User.objects.create(username=username, password=make_password(password))
        login(request, usr) 
        return redirect(reverse("main_page"))


def login_user(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = str(request.POST["username"])  
        password = str(request.POST["password"])  
        print(username)
        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            return render(request, "login.html", context={"error": "Логин или пароль не совпадают!"})
        login(request, user)
        return redirect(reverse("main_page"))

def logout_user(request):
    logout(request)
    return redirect(reverse("main_page"))


def main_page(request):
    if request.method == 'GET':    
        return render(
                            request=request,
                            template_name="main_page.html",
                            context={}
            )
    if request.method == 'POST':
        title = request.POST["title"]
        description = request.POST["description"]
        date = datetime.strptime(request.POST["date"],"%Y-%m-%d")
        alco = models.AlcoQR.objects.create(
            title = title,
            description = description,
            date = date
        )
        print(title,description,date)
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(f"http://127.0.0.1:8000/alco{alco.id}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        image_path = (f"static/media/images/alco_qr_{alco.id}.png")

        # Сохраняем QR-код на сервере
        img.save(image_path)

        # Сохраняем путь к изображению в поле модели
        alco.images = (f"/images/alco_qr_{alco.id}.png")
        alco.save()
        return render(
                            request=request,
                            template_name="main_page.html",
                            context={"id":alco.id}
            )

def alco_index(request,pk):
    product = models.AlcoQR.objects.get(id=pk)
    return render(
                            request=request,
                            template_name="QRPage.html",
                            context={"product":product}
            )
