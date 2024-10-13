from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Courses,Categories,Chapters,Videoes,Knowledges
from .serializers import CoursesSerializer,CategoriesSerializer,KnowledgesSerializer,VideoesSerializer,ChaptersDetailSerializer

# Create your views here.
class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    #permission_classes = [permissions.IsAuthenticated]

class KnowledgesViewSet(viewsets.ModelViewSet):
    queryset=Knowledges.objects.all()
    serializer_class = KnowledgesSerializer
    #permission_classes = [permissions.IsAuthenticated]

class ChaptersViewSet(viewsets.ModelViewSet):
    queryset=Chapters.objects.all()
    serializer_class = ChaptersDetailSerializer
    #permission_classes = [permissions.IsAuthenticated]

class VideoesViewSet(viewsets.ModelViewSet):
    queryset=Videoes.objects.all()
    serializer_class = VideoesSerializer
    #permission_classes = [permissions.IsAuthenticated]

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
   # permission_classes = [permissions.IsAuthenticated]


    
    