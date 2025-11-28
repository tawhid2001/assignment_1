from django.shortcuts import render, get_object_or_404
from .models import Course, Trainer, Student


def courses(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'academy/courses.html', context)


def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    context = {
        'course': course
    }
    return render(request, 'academy/course_detail.html', context)

def course_edit(request, id):
    course= get_object_or_404(Course, id=id)
    context = {
        'course': course
    }
    return render(request, 'academy/course_edit.html', context)

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