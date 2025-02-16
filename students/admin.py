from django.contrib import admin
from .models import Student, Subject, Enrollment

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Enrollment)
