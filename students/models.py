from django.db import models

# ตารางนักเรียน


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# ตารางวิชาเรียน


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# ตารางการลงทะเบียนเรียน


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    enroll_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}"
