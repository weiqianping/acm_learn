from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
#https://blog.csdn.net/happygjcd/article/details/102649947
class UserProfile(AbstractUser):
    avatar_url = models.URLField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    sex = models.CharField(
        max_length=10,
        choices=(('male', '男'), ('female', '女')),
        default='female'
    )
    cellphone = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        verbose_name_plural = '自定义用户表'
    def __str__(self):
        return self.username
    
class StudentsProfile(models.Model):
    #id、学号、学院、专业、班级、个人简介
    id = models.OneToOneField(UserProfile, primary_key=True, on_delete=models.CASCADE)
    number = models.CharField(max_length=20, null=True, blank=True)
    college = models.CharField(max_length=50, null=True, blank=True)
    major = models.CharField(max_length=50, null=True, blank=True)
    class_name = models.CharField(max_length=50, null=True, blank=True)
    resume = models.TextField(null=True, blank=True)

class TeachersProfile(models.Model):
    #id、工号、学院、个人简介
    id = models.OneToOneField(UserProfile, primary_key=True, on_delete=models.CASCADE)
    number = models.CharField(max_length=20, null=True, blank=True)
    college = models.CharField(max_length=50, null=True, blank=True)
    resume = models.TextField(null=True, blank=True)