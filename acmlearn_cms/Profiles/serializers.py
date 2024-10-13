from rest_framework import serializers
from .models import TeachersProfile
from django.contrib.auth.models import User

class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeachersProfile
        fields='__all__'
