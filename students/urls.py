from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.index, name='index'),

    # Student URLs
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_add, name='student_add'),
    path('students/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),


    # Subject URLs
    path('subjects/', views.subject_list,
         name='subject_list'),  # แสดงรายการวิชา
    path('subjects/add/', views.subject_add,
         name='subject_add'),  # เพิ่มวิชาใหม่
    path('subjects/<int:pk>/edit/', views.subject_edit,
         name='subject_edit'),  # แก้ไขวิชาตาม ID
    path('subjects/<int:pk>/delete/', views.subject_delete,
         name='subject_delete'),  # ลบวิชาตาม ID

    # Enrollment URLs
    # Enrollment URLs
    path('enrollments/', views.enrollment_list, name='enrollment_list'),
    path('enrollments/add/', views.enrollment_add, name='enrollment_add'),
    path('enrollments/<int:pk>/delete/',
         views.enrollment_delete, name='enrollment_delete'),

]
