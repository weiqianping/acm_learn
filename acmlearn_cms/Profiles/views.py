from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken  # 如果使用 JWT 认证
from .models import UserProfile, StudentsProfile, TeachersProfile
from .serializers import UserProfileSerializer, StudentsProfileSerializer, TeachersProfileSerializer

# 注册视图
class RegisterView(APIView):
    def post(self, request):
        # 使用 UserProfileSerializer 处理数据
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            # 序列化器验证通过，保存用户信息
            serializer.save()
            return Response({'message': '用户注册成功！'}, status=status.HTTP_201_CREATED)
        # 验证失败
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 登录视图
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        # 通过用户名和密码验证
        user = authenticate(username=username, password=password)
        if user:
            # 生成 JWT 令牌
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': '登录成功！'
            }, status=status.HTTP_200_OK)
        # 验证失败
        return Response({'error': '用户名或密码错误'}, status=status.HTTP_401_UNAUTHORIZED)
