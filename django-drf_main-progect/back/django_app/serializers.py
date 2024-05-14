from django.contrib.auth.models import User, Group
from rest_framework import serializers ,pagination
from django_app import models



class CatagoryStartapSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryStartap
        fields = "__all__"

class FilesStartapSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FilesStartap
        fields = ('id' ,'startap', 'file')

class LikeStartapSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    def get_username(self,obj):
        return obj.author.username
    class Meta:
        model = models.LikeStartap
        fields = "__all__"

class StartapHardSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    category_title = serializers.SerializerMethodField()
    category_slug = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()
    files = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    def get_category_title(self, obj):
        return obj.category.title
    
    def get_category_slug(self, obj):
        return obj.category.slug

    def get_profile(self, obj):
        return {
            'name': obj.user.profile.name,
            'surname': obj.user.profile.surname,
            'number': obj.user.profile.number,
            "avatar" : obj.user.profile.avatar.url
        }

    def get_files(self, obj):
        files = models.FilesStartap.objects.filter(startap=obj)
        return FilesStartapSerializer(files, many=True).data
    
    def get_likes(self, obj):
        likes = models.LikeStartap.objects.filter(startap=obj)
        return LikeStartapSerializer(likes, many=True).data
    
    def get_likes_count(self, obj):
        likes = models.LikeStartap.objects.filter(startap=obj)
        return len(LikeStartapSerializer(likes, many=True).data)
    
    class Meta:
        model = models.Startap
        fields = '__all__'

class StartapSerializer(serializers.ModelSerializer):
    category = CatagoryStartapSimpleSerializer()
    
    class Meta:
        model = models.Startap
        fields = '__all__'

class ProfileSimpleSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)
    startap = serializers.SerializerMethodField()

    def get_startap(self,obj):
        user = User.objects.get(id = obj.user_id)
        startaps = models.Startap.objects.filter(user = user)
        return StartapSerializer(startaps, many=True).data




    class Meta:
        model = models.Profile
        fields = '__all__'