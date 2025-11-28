from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Trainer, Student
from .forms import CourseForm, TrainerForm, StudentForm
from django.contrib.auth.decorators import permission_required, login_required

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

@login_required
@permission_required('academy.change_course', raise_exception=True)
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

@login_required
@permission_required('academy.delete_course', raise_exception=True)
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

@login_required
@permission_required('academy.add_course', raise_exception=True)
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

@login_required
def trainers(request):
    trainers= Trainer.objects.all()
    context = {
        'trainers': trainers
    }
    return render(request, 'academy/trainers.html', context)

@login_required
@permission_required('academy.add_trainer', raise_exception=True)
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


@login_required
def trainer_detail(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    context = {
        'trainer': trainer
    }
    return render(request, 'academy/trainer_detail.html', context)


@login_required
@permission_required('academy.change_trainer', raise_exception=True)
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


@login_required
@permission_required('academy.delete_trainer', raise_exception=True)
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

# -----------------------------------------------------------------

def students(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'academy/students.html', context)


@login_required
@permission_required('academy.add_student', raise_exception=True)
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('academy:students')
    else:
        form = StudentForm()
        
    context = {
        'form': form
    }
    return render(request, 'academy/student_add.html', context)

@login_required
def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    context = {
        'student': student
    }
    return render(request, 'academy/student_detail.html', context)

@login_required
@permission_required('academy.change_student', raise_exception=True)
def student_edit(request, id):
    student= get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('academy:student_detail', id=student.id)
    else:
        form = StudentForm(instance=student)
    context = {
        'form': form,
        'student': student,
        'is_edit': True
    }
    return render(request, 'academy/student_edit.html', context)  


@login_required
@permission_required('academy.delete_student', raise_exception=True)
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        if student.student_photo and student.student_photo.url != '/media/default.png':
            student.student_photo.delete()
        student.delete()
        return redirect('academy:students')
    context = {
        'student': student
    }
    return render(request, 'academy/student_delete.html', context)  