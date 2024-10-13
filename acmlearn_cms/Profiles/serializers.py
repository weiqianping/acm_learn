from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import UserProfile, StudentsProfile, TeachersProfile

class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'password', 'email', 'avatar_url', 'avatar', 'birthday', 'sex', 'cellphone']
    
    def create(self, validated_data):
        # 在创建用户时对密码进行加密
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserProfileSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        # 更新时如果提供了密码，则需要加密
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super(UserProfileSerializer, self).update(instance, validated_data)

class StudentsProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsProfile
        fields = ['id', 'number', 'college', 'major', 'class_name', 'resume']

class TeachersProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachersProfile
        fields = ['id', 'number', 'college', 'resume']
