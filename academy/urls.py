from django.urls import path
from . import views

app_name = 'academy'

urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('trainers/', views.trainers, name='trainers'),
    path('students/', views.students, name='students'),
]
