from django.shortcuts import render
from rest_framework import viewsets
from . models import Student, Course, Grade
from .  serializer import StudentSerializer, CourseSerializer, GradeSerializer


# create class views
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer



# Create functions views here.
def dashboard(request):
    return render(request, 'portal/dashboard.html')