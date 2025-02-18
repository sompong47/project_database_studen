from django import forms
from .models import Enrollment, Student, Subject


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'grade', 'email']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'teacher']


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'subject']

    student = forms.ModelChoiceField(
        queryset=Student.objects.all(), empty_label="เลือกนักเรียน")
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all(), empty_label="เลือกวิชา")
