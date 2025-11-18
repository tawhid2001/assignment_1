from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    description = models.TextField()
    duration_weeks = models.IntegerField()
    course_image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    
class Trainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    expertise = models.CharField(max_length=200)
    trainer_photo = models.ImageField(upload_to='trainer_photos/', null=True, blank=True)
    
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    enrolled_courses = models.ManyToManyField(Course, related_name='enrolledstudents')
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, related_name='trainer_students')
