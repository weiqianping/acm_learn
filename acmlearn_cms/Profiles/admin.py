from django.contrib import admin
from .models import UserProfile, StudentsProfile, TeachersProfile

# Register your models here.
class StudentsProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'college', 'major', 'class_name', 'resume']
    list_per_page = 50

admin.site.register(StudentsProfile, StudentsProfileAdmin)

class TeachersProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'college', 'resume']
    list_per_page = 50
    
admin.site.register(TeachersProfile, TeachersProfileAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff', 'is_active', 'date_joined']
    list_filter = ['is_staff', 'is_active']
    list_per_page = 50

admin.site.register(UserProfile, UserProfileAdmin)