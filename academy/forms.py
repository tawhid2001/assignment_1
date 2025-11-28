from django import forms
from .models import Course, Trainer, Student


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'