from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from .models import EmailVerifyRecord, UserProfile
from .serializers import UserProfileSerializer, EmailVerifyRecordSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

@api_view(['POST'])
@permission_classes([AllowAny])
def send_email_verify_code(request):
    email = request.data.get('email')
    if not email:
        return Response({'error': '邮箱不能为空'}, status=status.HTTP_400_BAD_REQUEST)
    
    # 生成随机验证码
    code = get_random_string(6, '0123456789')
    EmailVerifyRecord.objects.update_or_create(email=email, defaults={'code': code})
    
    # 发送邮件
    send_mail(
        'Your verification code',
        f'Your verification code is: {code}',
        [email],
        fail_silently=False,
    )

    return Response({'message': '验证码已发送'}, status=status.HTTP_200_OK)
    

# 注册视图
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        email = request.data.get('email')
        code = request.data.get('code')
        if not EmailVerifyRecord.objects.filter(email=email, code=code).first():
            return Response({'error': 'Invalid verification code'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 修改密码视图
@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password(request):
    email = request.data.get('email')
    password = request.data.get('password')
    code = request.data.get('code')
    if not email or not password or not code:
        return Response({'error': '邮箱、密码和验证码不能为空'}, status=status.HTTP_400_BAD_REQUEST)

    # 验证验证码
    record = EmailVerifyRecord.objects.filter(email=email, code=code).first()
    if not record or not record.is_valid():
        return Response({'error': '验证码无效或已过期'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(email=email).first()
    if not user:
        return Response({'error': '用户不存在'}, status=status.HTTP_400_BAD_REQUEST)

    user.set_password(password)
    user.save()
    return Response({'message': '密码修改成功'}, status=status.HTTP_200_OK)

# 登录视图
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response({'error': '用户名和密码不能为空'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username, password=password)
    if user:
        # 创建或获取 Token
        token, created = Token.objects.get_or_create(user=user)
        #print(token.key
        # 使用序列化器将 user 对象转换为 JSON 格式
        userprofile_serializer = UserProfileSerializer(user)
        return Response({"token": token.key, "user": userprofile_serializer.data}, status=status.HTTP_200_OK)
        #return Response({'message': '登录成功'}, status=status.HTTP_200_OK)
    return Response({'error': '用户名或密码错误'}, status=status.HTTP_400_BAD_REQUEST)
