from django.db import models
from django.contrib.auth.models import User
from Profiles.models import TeachersProfile
from django.conf import settings

class Categories(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Knowledges(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Courses(models.Model):
    title = models.CharField(max_length=100)
    description=models.TextField()
    teacher=models.ForeignKey(TeachersProfile,related_name='courses',on_delete=models.CASCADE)
    category=models.ManyToManyField(Categories,related_name="courses")
    difficulty=models.CharField(max_length=20)
    cover=models.ImageField(upload_to='courses/',null=True,blank=True)
    cover_url=models.URLField(null=True,blank=True)
    duration=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    clicks=models.IntegerField(default=0)
    average_rating=models.FloatField(default=0)
    def __str__(self):
        return self.title

class Chapters(models.Model):
    course=models.ForeignKey(Courses,related_name='chapters',on_delete=models.CASCADE)
    knowledge=models.ManyToManyField(Knowledges,related_name="chapters")
    title=models.CharField(max_length=100)
    order=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Videoes(models.Model):
    chapter=models.ForeignKey(Chapters,related_name="videoes",on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    video=models.FileField(upload_to='videoes/')
    video_url=models.URLField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


    