from django.test import TestCase

# Create your tests here.
"""
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from rest_framework import status
from .models import Courses, Chapters, Videoes, Categories, Knowledges
from Profiles.models import TeachersProfile
from django.contrib.auth.models import User
import tempfile
import os

class CourseAPITest(TestCase):
    def setUp(self):
        # 初始化测试数据
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.teacher_profile = TeachersProfile.objects.create(user=self.user, bio='Test Bio')
        self.category = Categories.objects.create(name='Test Category', description='Test Description')
        self.knowledge = Knowledges.objects.create(name='Test Knowledge', description='Test Description')

        # 创建一个临时文件用于上传
        self.temp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        self.temp_file.write(b'test content')
        self.temp_file.seek(0)

    def tearDown(self):
        # 清理临时文件
        self.temp_file.close()

    def test_create_course(self):
        # 测试创建课程
        course_data = {
            'title': 'Test Course',
            'description': 'Test Description',
            'teacher': self.teacher_profile.id,
            'category': [self.category.id],
            'difficulty': 'Beginner',
            'cover': self.temp_file,
            'duration': 120,
        }
        response = self.client.post('/api/courses/', course_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Courses.objects.count(), 1)
        self.assertEqual(Courses.objects.get().title, 'Test Course')

    def test_create_chapter(self):
        # 测试创建章节
        course = Courses.objects.create(
            title='Test Course',
            description='Test Description',
            teacher=self.teacher_profile,
            difficulty='Beginner',
            duration=120,
        )
        course.category.add(self.category)

        chapter_data = {
            'course': course.id,
            'knowledge': [self.knowledge.id],
            'title': 'Test Chapter',
            'order': 1,
        }
        response = self.client.post('/api/chapters/', chapter_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Chapters.objects.count(), 1)
        self.assertEqual(Chapters.objects.get().title, 'Test Chapter')

    def test_create_video(self):
        # 测试创建视频
        course = Courses.objects.create(
            title='Test Course',
            description='Test Description',
            teacher=self.teacher_profile,
            difficulty='Beginner',
            duration=120,
        )
        course.category.add(self.category)

        chapter = Chapters.objects.create(
            course=course,
            title='Test Chapter',
            order=1,
        )
        chapter.knowledge.add(self.knowledge)

        video_data = {
            'chapter': chapter.id,
            'title': 'Test Video',
            'video': self.temp_file,
        }
        response = self.client.post('/api/videoes/', video_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Videoes.objects.count(), 1)
        self.assertEqual(Videoes.objects.get().title, 'Test Video')

    def test_update_course(self):
        # 测试更新课程
        course = Courses.objects.create(
            title='Test Course',
            description='Test Description',
            teacher=self.teacher_profile,
            difficulty='Beginner',
            duration=120,
        )
        course.category.add(self.category)

        updated_data = {
            'title': 'Updated Course',
            'description': 'Updated Description',
            'teacher': self.teacher_profile.id,
            'category': [self.category.id],
            'difficulty': 'Intermediate',
            'duration': 150,
        }
        response = self.client.put(f'/api/courses/{course.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Courses.objects.get(id=course.id).title, 'Updated Course')

    def test_delete_course(self):
        # 测试删除课程
        course = Courses.objects.create(
            title='Test Course',
            description='Test Description',
            teacher=self.teacher_profile,
            difficulty='Beginner',
            duration=120,
        )
        course.category.add(self.category)

        response = self.client.delete(f'/api/courses/{course.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Courses.objects.count(), 0)
        
        python manage.py test
"""