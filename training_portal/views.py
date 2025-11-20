from django.shortcuts import render
from academy.models import Course, Trainer, Student

# Create your views here.
def home(request):
    total_courses = Course.objects.count()
    total_trainers = Trainer.objects.count()
    total_students = Student.objects.count()
    context = {
        'total_courses': total_courses,
        'total_trainers': total_trainers,
        'total_students': total_students,
    }
    return render(request, 'home.html', context)