from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE) # authentication will be implemented
    reg_num = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.name.username
    
    def get_absoluet_url(self):
        return reverse('portal:router') # will change as the development progressess
   


class Course(models.Model):
    title = models.CharField(max_length = 50, unique=True)
    code = models.CharField(max_length = 15, unique = True)
    tutor = models.CharField(max_length= 100, null=True)
    content = models.TextField(unique=True)

    def __str__(self):
        return self.title
    
    def get_absoluet_url(self):
        return reverse('portal:router') # will change as the development progressess
   


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete= models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return str(self.student.name.username)
    
    def get_absoluet_url(self):
        return reverse('portal:router') # will change as the development progressess
   
