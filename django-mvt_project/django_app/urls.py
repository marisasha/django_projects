from django.contrib import admin
from django.urls import include, path
from django_app import views,views_a

urlpatterns = [
    path('',views.login_user,name = 'login_user'),
    path('logout_user',views.logout_user,name = 'logout_user'),
    path('register_1',views.register_1,name = 'register_1'),
    path('register_2',views.register_2,name = 'register_2'),

    path('my_profile',views.my_profile,name = 'my_profile'),
    path('find_friends',views.find_friends,name = 'find_friends'),
    path('profile/<str:user_id>',views.profile,name = 'profile'),

    path('application_to_user/<str:user_id>',views.application_to_user,name = 'application_to_user'),
    path('accept_application_to_user/<str:user_id>',views.accept_application_to_user,name = 'accept_application_to_user'),
    path('chats',views.chats,name='chats'),
    path('get_or_create_chat/<str:user_id>',views.get_or_create_chat,name='get_or_create_chat'),
    path("chat/<slug:chat_slug>/<slug:user_id>", views.chat, name="chat"),
    path('news',views.news,name='news'),
    path('new_post',views.new_post,name='new_post'),

    
]

websocket_urlpatterns = [path("ws/chat/<slug:room_name>/", views_a.ChatConsumer.as_asgi())]
