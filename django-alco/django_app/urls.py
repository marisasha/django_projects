from django.contrib import admin
from django.urls import include, path
from django_app import views

urlpatterns = [
    path('login_user',views.login_user,name = 'login_user'),
    path('logout_user',views.logout_user,name = 'logout_user'),
    path('register',views.register,name = 'register'),

    path('',views.main_page,name = 'main_page'),
    path('alco<str:pk>',views.alco_index,name = 'alco_index')

]
