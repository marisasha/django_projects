import datetime
from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser , IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from django_app import models, serializers , utils
from django.db.models import QuerySet
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User




def index(request):
    return render(
        request,
        "index.html",
        context={}
    )


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])  
def api(request: Request) -> Response:
    return Response(
        data={
            "message":"ok"
        },
        status=status.HTTP_200_OK
    )
@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])  
def api_startap_with_need_category(request:Request,slug:str,id:str) -> Response:
    _data = models.Startap.objects.get(id = id)
    _data_serialize = serializers.StartapHardSerializer(_data,many = True if isinstance(_data,QuerySet) else False).data
    _data_serialize_with_cache = utils.Cache.get_cache(key = "startap_cache",query = lambda : _data_serialize, timeout = 1)
    return Response(
        data = {
            "data":_data_serialize_with_cache
        },
        status=status.HTTP_200_OK
    )

@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])  
def api_startaps_with_need_category(request:Request,slug) -> Response:
    _category = models.CategoryStartap.objects.get(slug = slug)
    _data = models.Startap.objects.filter(category = _category.id)
    _data_serialize = serializers.StartapHardSerializer(_data, many=True if isinstance(_data, QuerySet) else False).data
    _data_serialize_with_cache = utils.Cache.get_cache(key="startaps_cache", query=lambda: _data_serialize, timeout=1)
    return Response(
        data = {
            "data":_data_serialize_with_cache
        },
        status=status.HTTP_200_OK
    )


@api_view(http_method_names=["POST"])
@permission_classes([AllowAny])
def api_user_register(request: Request) -> Response:
    username = str(request.data.get("username", None))
    password = str(request.data.get("password", None))
    if username and password:
        User.objects.create(username=username, password=make_password(password))
        return Response(data={"success": "Account succesfully created!"}, status=status.HTTP_200_OK)
    else:
        return Response(data={"error": "Login or password is incorrect"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])
def api_profile(request: Response,username:str) ->Response:
    _user = User.objects.get(username = username)
    _data = models.Profile.objects.get(user = _user )
    _data_serialize = serializers.ProfileSimpleSerializer(_data,many = True if isinstance(_data,QuerySet) else False).data
    _data_serialize_with_cache = utils.Cache.get_cache(key = "profile_cache",query = lambda : _data_serialize, timeout = 2)
    return Response(
        data = {
            "data":_data_serialize_with_cache
        },
        status=status.HTTP_200_OK
    )



@api_view(http_method_names=["POST"])
@permission_classes([AllowAny])
def api_create_profile(request: Request) -> Response:
    try:
        _username = str(request.data.get("username",None))
        _name = str(request.data.get("name", None))
        _surname = str(request.data.get("surname", None))
        _number = str(request.data.get("number", None))    
        _avatar = request.FILES.get("avatar", None)
        _user = User.objects.get(username = _username)
        usr = models.Profile.objects.get(user = _user)
        print(_avatar)
        usr.name = _name
        usr.surname = _surname
        usr.number = _number
        if _avatar:
            usr.avatar = _avatar
        usr.save()
        return Response(data={"success": "Account successfully created!"}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(data={"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])  
def api_category_all(request: Response) -> Response:
    _data = models.CategoryStartap.objects.all()
    _data_serialize = serializers.CatagoryStartapSimpleSerializer(_data,many = True if isinstance(_data,QuerySet) else False).data
    _data_serialize_with_cache = utils.Cache.get_cache(key = "category_cache",query = lambda : _data_serialize, timeout = 10)
    return Response(
        data = {
            "data":_data_serialize_with_cache
        },
        status=status.HTTP_200_OK
    )
@api_view(http_method_names=["GET","POST"])
@permission_classes([AllowAny])  
def api_create_startap(request:Request) -> Response:
    if request.method == "GET":
        return Response(
        data={
            "message":"ok"
        },
        status=status.HTTP_200_OK
    )
    if request.method == "POST":
        _username = str(request.data.get("username",None))
        _category_id = request.data.get("category",None)
        _title = request.data.get("title",None)
        _description = request.data.get("description",None)
        _location = request.data.get("location",None)
        _deposit_amount = request.data.get("deposit_amount",None)
        _image = request.FILES.get("image", None)
        _pdf = request.FILES.get("pdf", None)
        _file = request.FILES.get("file", None)
        _user = User.objects.get(username = _username)
        _category = models.CategoryStartap.objects.get(id = _category_id)
        print("\n\n\n\n\n\n",_category,_username,_title,_location,_image,_file,"\n\n\n\n\n\n\n\n")
        startap = models.Startap.objects.create(
            user = _user,
            category = _category,
            title = _title,
            description = _description,
            location = _location,
            deposit_amount = _deposit_amount
        )

        if _image:
            startap.image = _image
            startap.save()
        if _pdf:
            startap.pdf = _pdf
            startap.save()
        files_of_startap = models.FilesStartap.objects.create(startap=startap)
        if _file:
            files_of_startap.file = _file
            files_of_startap.save()

        return Response(
            data={
                "message":"Startap succesfull!"
            },
            status=status.HTTP_200_OK
        )

@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])  
def api_create_like(request: Response,startap_id:int,username:str) -> Response:
    _user = User.objects.get(username = username)
    _startap = models.Startap.objects.get(id = startap_id)
    try:
        _like_startap = models.LikeStartap.objects.get(startap = _startap,author = _user )
        _like_startap.delete()
        return Response(
            data={
                "message":"Like has been delete!"
            },
            status=status.HTTP_200_OK
        )
    except Exception as _:
        models.LikeStartap.objects.create(startap = _startap , author = _user)
        return Response(
            data={
                "message":"Like has been set!"
            },
            status=status.HTTP_200_OK
        )
