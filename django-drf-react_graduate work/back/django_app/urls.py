from django.contrib import admin
from django.urls import path
from django_app import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path("",view = views.index),
    # 
    path("api",view=views.api),
    # 
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/register", view = views.api_user_register),
    path("api/register2", view = views.api_create_profile),
    #  
    path("api/profile/<str:username>",view=views.api_profile),
    path("api/category",view=views.api_category_all),
    path("api/create-startap",view=views.api_create_startap),
    path("api/<str:slug>",view=views.api_startaps_with_need_category),
    path("api/<slug:slug>/<int:id>",view=views.api_startap_with_need_category),
    path("api/press_like/<int:startap_id>/<str:username>",view=views.api_create_like),
]
