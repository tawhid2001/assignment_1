from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Trainer, Student
from .forms import CourseForm, TrainerForm

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


def course_delete(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        if course.course_image and course.course_image.url != '/media/default.png':
            course.course_image.delete()
        course.delete()
        return redirect('academy:courses')
    context = {
        'course': course
    }
    return render(request, 'academy/course_delete.html', context)


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


# -----------------------------------------------------------------------
def trainers(request):
    trainers= Trainer.objects.all()
    context = {
        'trainers': trainers
    }
    return render(request, 'academy/trainers.html', context)


def trainer_add(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('academy:trainers')
    else:
        form = TrainerForm()
        
    context = {
        'form': form
    }
    return render(request, 'academy/trainer_add.html', context)

def trainer_detail(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    context = {
        'trainer': trainer
    }
    return render(request, 'academy/trainer_detail.html', context)

def students(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'academy/students.html', context)