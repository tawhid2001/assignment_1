from django.contrib import admin
from .models import Course, Trainer, Student

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'duration_weeks')
    search_fields = ('course_name','students')
    list_filter = ('duration_weeks','enrolled_students')

class TrainerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'expertise')
    search_fields = ('full_name', 'email')
    list_filter = ('expertise','students')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'trainer', 'is_active')
    search_fields = ('full_name', 'email')
    list_filter = ('is_active','enrolled_courses','trainer')
    
    
admin.site.register(Course, CourseAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Student, StudentAdmin)