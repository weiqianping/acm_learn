from django.urls import path
from .views import send_email_verify_code, register, login, reset_password

urlpatterns = [
    path('send_email_verify_code/', send_email_verify_code, name='send_email_verify_code'),
    path('register/', register, name='register'),
    path('reset_password/', reset_password, name='reset_password'),
    path('login/', login, name='login'),
]