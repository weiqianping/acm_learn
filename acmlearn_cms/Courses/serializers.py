from rest_framework import serializers
from .models import Courses,Chapters,Videoes,Categories,Knowledges
from Profiles.models import TeachersProfile
from Profiles.serializers import TeacherProfileSerializer

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categories
        fields=('id','name','description')

class KnowledgesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Knowledges
        fields=('id','name','description')

class CoursesSerializer(serializers.ModelSerializer):
    teacher=TeacherProfileSerializer()
    category=CategoriesSerializer()
    class Meta:
        model=Courses
        fields=('id','title','cover','cover_url','description','difficulty','duration','teacher','average_rating','clicks','category')


class ChaptersDetailSerializer(serializers.ModelSerializer):
    course=CoursesSerializer()
    knowledge=KnowledgesSerializer(many=True)
    class Meta:
        model=Chapters
        fields=('id','title','order','course','knowledge')

class VideoesSerializer(serializers.ModelSerializer):
    chapter=ChaptersDetailSerializer()
    class Meta:
        model=Videoes
        fields=('id','title','chapter','video','video_url')
