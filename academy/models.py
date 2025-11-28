from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    description = models.TextField()
    duration_weeks = models.IntegerField()
    course_image = models.ImageField(upload_to='course_images/', default='default.png')
    
    def __str__(self):
        return self.course_name
    
class Trainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    expertise = models.CharField(max_length=200)
    trainer_photo = models.ImageField(upload_to='trainer_photos/', default='default.png')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    student_photo = models.ImageField(upload_to='student_photos/', default='default.png')
    enrolled_courses = models.ManyToManyField(Course, related_name='enrolled_students')
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, related_name='students')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"