from django.contrib import admin
from . models import Student, Course, Grade

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'reg_num')
    list_filter = ('name', 'reg_num')
    search_fields =('name', 'reg_num')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'tutor')
    list_filter = ('tutor', 'code', 'title')
    search_fields = ('title', 'code', 'tutor', 'content')


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'grade')
    list_filter =  ('student', 'grade', 'course')
    search_fields = ('student', 'grade', 'course')