from django.urls import path
from . import views

app_name = 'academy'

urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('course/<int:id>/', views.course_detail, name='course_detail'),
    path('course/edit/<int:id>/', views.course_edit, name='course_edit'),
    path('trainers/', views.trainers, name='trainers'),
    path('students/', views.students, name='students'),
]
