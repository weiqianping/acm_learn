from rest_framework import serializers
from .models import EmailVerificationCode, Profile
from django.contrib.auth.models import User

class EmailVerificationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailVerificationCode
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id', 'username', 'email']
        ref_name = 'UserSerializerForProfiles'  # 显式设置 ref_name

class ProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'avatar', 'avatar_url', 'birthday', 'sex', 'cellphone']

    def update(self, instance, validated_data):
        user = instance.user

        # Update User fields
        user.username = validated_data.pop('username', user.username)
        user.email = validated_data.pop('email', user.email)
        user.save()

        # Update Profile fields
        avatar = validated_data.pop('avatar', None)
        if avatar:
            instance.avatar = avatar

        # Update other Profile fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        #instance.save()

        return instance