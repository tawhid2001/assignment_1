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


def trainer_edit(request, id):
    trainer= get_object_or_404(Trainer, id=id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('academy:trainer_detail', id=trainer.id)
    else:
        form = TrainerForm(instance=trainer)
    context = {
        'form': form,
        'trainer': trainer,
        'is_edit': True
    }
    return render(request, 'academy/trainer_edit.html', context)


def trainer_delete(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    if request.method == 'POST':
        if trainer.trainer_photo and trainer.trainer_photo.url != '/media/default.png':
            trainer.trainer_photo.delete()
        trainer.delete()
        return redirect('academy:trainers')
    context = {
        'trainer': trainer
    }
    return render(request, 'academy/trainer_delete.html', context)

def students(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'academy/students.html', context)