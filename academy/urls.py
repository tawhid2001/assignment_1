from django.urls import path
from . import views

app_name = 'academy'

urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('course/<int:id>/', views.course_detail, name='course_detail'),
    path('course/edit/<int:id>/', views.course_edit, name='course_edit'),
    path('course/add/', views.course_add, name='course_add'),
    path('course/delete/<int:id>/', views.course_delete, name='course_delete'),
    
    path('trainers/', views.trainers, name='trainers'),
    path('trainer/add/', views.trainer_add, name='trainer_add'),
    path('trainer/<int:id>/', views.trainer_detail, name='trainer_detail'),
    path('trainer/edit/<int:id>/', views.trainer_edit, name='trainer_edit'),
    path('trainer/delete/<int:id>/', views.trainer_delete, name='trainer_delete'),
    
    
    path('students/', views.students, name='students'),
    path('student/add/', views.student_add, name='student_add'),
    path('student/<int:id>/', views.student_detail, name='student_detail'),
    path('student/edit/<int:id>/', views.student_edit, name='student_edit'),
    path('student/delete/<int:id>/', views.student_delete, name='student_delete'),
]
