from django.contrib import admin
from .models import UserProfile, StudentsProfile, TeachersProfile

# Register your models here.
admin.register(UserProfile)
admin.register(StudentsProfile)
admin.register(TeachersProfile)