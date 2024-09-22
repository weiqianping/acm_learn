from django.test import TestCase
from django.urls import reverse
from .models import UserProfile

class UserProfileTestCase(TestCase):
    def setUp(self):
        # 创建测试用户
        self.user = UserProfile.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com'
        )

    def test_user_profile_creation(self):
        # 测试用户是否被正确创建
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')

    def test_user_profile_view(self):
        # 测试访问用户资料视图
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')