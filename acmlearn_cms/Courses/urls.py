from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CoursesViewSet,ChaptersViewSet,VideoesViewSet,CategoriesViewSet,KnowledgesViewSet
from django.conf import settings
from django.conf.urls.static import static

router=DefaultRouter()
router.register('courses',CoursesViewSet)
router.register('chapters',ChaptersViewSet)
router.register('videoes',VideoesViewSet)
router.register('categories',CategoriesViewSet)
router.register('knowledges',KnowledgesViewSet)
urlpatterns=[
    path('',include(router.urls)),
    #path('categories/',CategoriesView.as_view()),
]