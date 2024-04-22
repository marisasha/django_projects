from django.shortcuts import render
from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.cache import caches
from django_app import models
from django_settings import utils
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import Q

def register_1(request):
    if request.method == "GET":
        return render(request, "Register.html")
    elif request.method == "POST":
        username = str(request.POST["username"])
        password = str(request.POST["password"])
        password_accept = str(request.POST["password_accept"])
        if password != password_accept:
            return render(request, "Register.html", context={"error": "Пароли не совпадают!"})
        usr = User.objects.create(username=username, password=make_password(password))
        login(request, usr) 
        return redirect(reverse("register_2"))

def register_2(request):
    if request.method == "GET":
        return render(request, "Register2.html")
    elif request.method == "POST":
        user = request.user
        user_name = request.POST["name"]
        user_surname = request.POST["surname"]
        user_description = request.POST.get("description","")
        user_avatar = request.FILES.get("avatar", None)
        usr = models.Profile.objects.filter(user = user).first()
        usr.name = user_name
        usr.surname = user_surname
        usr.description = user_description
        if user_avatar != None:    
            usr.avatar = user_avatar
        usr.save()
    return redirect(reverse("my_profile"))



def login_user(request):
    if request.method == "GET":
        return render(request, "Login.html")
    elif request.method == "POST":
        username = str(request.POST["username"])  
        password = str(request.POST["password"])  
        print(username)
        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            return render(request, "Login.html", context={"error": "Логин или пароль не совпадают!"})
        login(request, user)
        return redirect(reverse("my_profile"))

def logout_user(request):
    logout(request)
    return redirect(reverse("login_user"))


def my_profile(request):
    now_user = request.user
    friends = models.Friends.objects.filter(user = now_user)
    user_news = models.News.objects.filter(user=now_user)
    now_user_news = []
    count = 0
    for news in user_news:
        now_user_news.append({
            "user": news.user,
            "content": news.content,
            "image": news.image,
            "date": news.date_added
        })
        count+=1
    now_user_news = sorted(now_user_news, key=lambda x: x['date'],reverse=True)
    return render(
                            request=request,
                            template_name="MyProfile.html",
                            context={"friends":friends,"now_user_news":now_user_news}
            )

def profile(request,user_id):
    now_user = request.user
    page_user = models.User.objects.get(id = user_id)
    user_friends = models.Friends.objects.filter(user = page_user)
    is_now_user_and_page_user_friends = False
    for users in user_friends:
        for user in users.friends.all():
            if user == now_user:
                is_now_user_and_page_user_friends = True


    _applications_to_friend = models.ApplicationFriends.objects.get(user = page_user)
    is_user_in_application_to_user_for_page_user = False
    for user in _applications_to_friend.application.all():
            if user == now_user:
                is_user_in_application_to_user_for_page_user = True
    
    _applications_to_friend = models.ApplicationFriends.objects.get(user = now_user)
    is_user_in_application_to_user_for_now_user = False
    for user in _applications_to_friend.application.all():
            if user == page_user:
                is_user_in_application_to_user_for_now_user = True

    

    return render(
                            request=request,
                            template_name="Profile.html",
                            context={
                                    "user":page_user,
                                    "user_friends":user_friends,
                                    "is_user_in_application_to_user_for_page_user":is_user_in_application_to_user_for_page_user,
                                    "is_user_in_application_to_user_for_now_user":is_user_in_application_to_user_for_now_user,
                                    "is_now_user_and_page_user_friends":is_now_user_and_page_user_friends
                                }
            )

def find_friends(request):
    if request.method == "GET":
        now_user = request.user
        friends = models.Friends.objects.filter(user = now_user)
        _applications_to_friend = models.ApplicationFriends.objects.filter(user = now_user)
        return render(
                            request=request,
                            template_name="Friends.html",
                            context={"friends":friends,"applications_to_friend":_applications_to_friend}
            )
    if request.method == "POST":
        search = request.POST.get("search","")
        users = models.Profile.objects.filter(Q(name__icontains=search) | Q(surname__icontains=search))
        return render(
                            request=request,
                            template_name="Friends.html",
                            context={"users":users}
            )
    


def application_to_user(request,user_id):
    now_user = request.user
    page_user = models.User.objects.get(id = user_id)
    application = models.ApplicationFriends.objects.get(user = page_user)
    application.application.add(now_user)
    return redirect(reverse("profile",args=(user_id,)))


def accept_application_to_user(request,user_id):
    now_user = request.user
    page_user = models.User.objects.get(id = user_id)

    now_user_friends = models.Friends.objects.get(user = now_user)
    now_user_friends.friends.add(page_user)
    
    page_user_friends = models.Friends.objects.get(user = page_user)
    page_user_friends.friends.add(now_user)

    try:
        now_user_application = models.ApplicationFriends.objects.get(user = now_user)
        now_user_application.application.remove(page_user)
        now_user_application.save()
    except Exception as error:
        print(f'accept_application_to_user:{error}')

    try:
        page_user_application = models.ApplicationFriends.objects.get(user = page_user)
        page_user_application.application.remove(now_user)
        page_user_application.save()
    except Exception as error:
        print(f'accept_application_to_user:{error}')

    return redirect(reverse("profile",args=(user_id,)))


def chats(request):
    user = request.user
    _rooms = models.Room.objects.filter(users=user)
    last_message = models.Message.objects.filter(user = user)[:1][::-1]
    for i in last_message:
        print(i)
    return render(
                        request=request,
                        template_name="Chats.html",
                        context={"rooms":_rooms,"last_message":last_message}
        )

def get_or_create_chat(request,user_id):
    now_user = request.user
    page_user = models.User.objects.get(id=user_id)
    try:
        _room = models.Room.objects.filter(users=now_user).filter(users=page_user).first()
        return redirect(reverse("chat",args=(_room.slug,user_id,)))
    except Exception:
        _room = models.Room.objects.create(
            name = 'userchat',
        )
        _room.slug = f'userchat{_room.id}'
        _room.users.add(user_id,now_user)
        _room.save()
        print(_room.users)
        return redirect(reverse("chat",args=(_room.slug,user_id,)))

def chat(request,chat_slug,user_id):
    page_user = models.User.objects.get(id = user_id)
    _room = models.Room.objects.get(slug=chat_slug)
    _messages = models.Message.objects.filter(room=_room)[:30][::-1]
    return render(request, "Chat.html", context={"room": _room, "messages": _messages,"page_user":page_user})

def news(request):
    now_user = request.user
    user_friends_news = models.Friends.objects.get(user=now_user)
    now_user_news = {}
    count = 0
    now_user_news = []
    count = 0
    for friend in user_friends_news.friends.all():
        friend_news = models.News.objects.filter(user=friend)
        for news in friend_news:
            now_user_news.append({
                "user": news.user,
                "content": news.content,
                "image": news.image,
                "date": news.date_added
            })
            count += 1
    user_news = models.News.objects.filter(user=now_user)
    for news in user_news:
        now_user_news.append({
            "user": news.user,
            "content": news.content,
            "image": news.image,
            "date": news.date_added
        })
        count+=1
    now_user_news = sorted(now_user_news, key=lambda x: x['date'],reverse=True)
    print(now_user_news)
    return render(
                        request=request,
                        template_name="News.html",
                        context={"now_user_news":now_user_news}
        )

def new_post(request):
    post_author = request.user
    post_content = request.POST["content"]
    post_image = request.FILES.get("image", None)
    post = models.News.objects.create(
        user = post_author,
        content = post_content,
        image = post_image
    )
    post.save()
    return redirect(reverse("news"))