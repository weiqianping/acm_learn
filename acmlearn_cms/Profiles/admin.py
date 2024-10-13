from django.contrib import admin
from .models import UserProfile, StudentsProfile, TeachersProfile

# Register your models here.
admin.site.register(StudentsProfile)
admin.site.register(TeachersProfile)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff', 'is_active', 'date_joined']
    list_filter = ['is_staff', 'is_active']
    list_per_page = 50

admin.site.register(UserProfile, UserProfileAdmin)