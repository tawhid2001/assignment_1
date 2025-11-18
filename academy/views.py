from django.shortcuts import render
from .models import Course, Trainer, Student

def courses(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'academy/courses.html', context)

def trainers(request):
    trainers= Trainer.objects.all()
    context = {
        'trainers': trainers
    }
    return render(request, 'academy/trainers.html', context)

def students(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'academy/students.html', context)