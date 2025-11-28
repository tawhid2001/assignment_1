from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Trainer, Student
from .forms import CourseForm

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
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('academy:course_detail', id=course.id)
    else:
        form = CourseForm(instance=course)
    context = {
        'form': form,
        'course': course,
        'is_edit': True
    }
    return render(request, 'academy/course_edit.html', context)


def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('academy:courses')
    else:
        form = CourseForm()
        
    context = {
        'form': form
    }
    return render(request, 'academy/course_add.html', context)

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