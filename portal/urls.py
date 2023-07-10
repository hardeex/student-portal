from . import views
from django.urls import path, include
from rest_framework import routers
from portal.views import StudentViewSet, CourseViewSet, GradeViewSet


router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'grades', GradeViewSet)

app_name = 'portal'
urlpatterns = [
    path('', include(router.urls), name='router'),
    path('portal/', views.dashboard, name='dashboard')
]