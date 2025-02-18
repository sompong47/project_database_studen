from .models import Student
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student, Subject, Enrollment
from django.db.models import Count
from .forms import StudentForm, SubjectForm, EnrollmentForm


def index(request):
    # Get counts for dashboard
    context = {
        'total_students': Student.objects.count(),
        'total_subjects': Subject.objects.count(),
        'total_enrollments': Enrollment.objects.count(),
    }
    return render(request, 'index.html', context)

# Student Views


# views.py

# แสดงรายชื่อนักเรียนและเพิ่มข้อมูล

def student_list(request):
    students = Student.objects.all()  # ดึงข้อมูลทั้งหมดจากตาราง Student

    if request.method == 'POST':  # เมื่อผู้ใช้งานส่งฟอร์ม
        form = StudentForm(request.POST)
        if form.is_valid():  # ถ้าฟอร์มถูกต้อง
            form.save()  # บันทึกข้อมูลลงฐานข้อมูล
            # รีเฟรชหน้าเพื่อแสดงข้อมูลที่อัพเดต
            return redirect('student_list')

    else:
        form = StudentForm()  # ถ้าไม่ได้ส่ง POST ก็แสดงฟอร์มเปล่า

    return render(request, 'student_list.html', {'students': students, 'form': form})


def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    messages.success(request, 'ลบนักเรียนสำเร็จ')
    return redirect('student_list')


def student_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        email = request.POST.get('email')

        Student.objects.create(
            name=name,
            age=age,
            grade=grade,
            email=email
        )
        messages.success(request, 'เพิ่มนักเรียนสำเร็จ')
        return redirect('student_list')

    return render(request, 'student_form.html')


def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.grade = request.POST.get('grade')
        student.email = request.POST.get('email')
        student.save()
        messages.success(request, 'แก้ไขข้อมูลนักเรียนสำเร็จ')
        return redirect('student_list')

    return render(request, 'student_form.html', {'student': student})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    messages.success(request, 'ลบนักเรียนสำเร็จ')
    return redirect('student_list')

# Subject Views


def subject_list(request):
    subjects = Subject.objects.all()
    form = SubjectForm()

    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'เพิ่มวิชาสำเร็จ')
            return redirect('subject_list')

    return render(request, 'subject_list.html', {'subjects': subjects, 'form': form})


def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    messages.success(request, 'ลบวิชาสำเร็จ')
    return redirect('subject_list')


def subject_add(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "เพิ่มวิชาใหม่สำเร็จ")
            return redirect('subject_list')  # เปลี่ยนหน้าไปที่หน้ารายการวิชา
    else:
        form = SubjectForm()
    return render(request, 'students/subject_form.html', {'form': form})


def subject_edit(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            messages.success(request, 'แก้ไขวิชาสำเร็จ')
            return redirect('subject_list')
    else:
        form = SubjectForm(instance=subject)

    return render(request, 'subject_list.html', {'form': form})
# Enrollment Views


def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollment_list.html', {'enrollments': enrollments})


def enrollment_add(request):
    if request.method == 'POST':
        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')

        # Check if enrollment already exists
        if not Enrollment.objects.filter(student_id=student_id, subject_id=subject_id).exists():
            Enrollment.objects.create(
                student_id=student_id,
                subject_id=subject_id
            )
            messages.success(request, 'เพิ่มการลงทะเบียนสำเร็จ')
        else:
            messages.error(request, 'นักเรียนได้ลงทะเบียนวิชานี้แล้ว')
        return redirect('enrollment_list')

    students = Student.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'students/enrollment_form.html', {  # ใส่ที่นี่
        'students': students,
        'subjects': subjects
    })


def enrollment_delete(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    enrollment.delete()
    messages.success(request, 'ยกเลิกการลงทะเบียนสำเร็จ')
    return redirect('enrollment_list')
