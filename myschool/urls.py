from django.contrib import admin
from django.urls import path, include
from myschool.views import ClassesViewset, TeacherViewset
from rest_framework import routers
from .views import AllStudentS, RegisterViewset, SendOtp, StudentAddressview, StudentAuth, StudentMarksView, TeacherAuthViews,DecodeToken,DecodeTokenS,TaskViewset,TeacherTask_Assigned,StudentTask_Assigned,ClassTaskViewset
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 

routers = routers.DefaultRouter()
routers.register(r'teacher-register',TeacherViewset, basename='teacher')
routers.register(r'student-register',RegisterViewset,basename='student')
routers.register(r'classes',ClassesViewset,basename='classes')

routers.register(r'teacher-auth',TeacherAuthViews, basename='teacher-auth')
routers.register(r'teacher-auth-decode',DecodeToken, basename='teacher_auth_decode')
routers.register(r'student-auth',StudentAuth, basename='Student-auth')
routers.register(r'student-auth-decode',DecodeTokenS, basename='student_auth_decode')


routers.register(r'teacher-task',TaskViewset, basename='task-teacher')
routers.register(r'teacher-assign-task',TeacherTask_Assigned, basename='teacher-assign-task')
routers.register(r'student-assign-task',StudentTask_Assigned, basename='student-assign-task')

routers.register(r'class_task',ClassTaskViewset,basename='class_task')

routers.register(r'student_marksview',StudentMarksView,basename='student_marksview')
routers.register(r'student_address',StudentAddressview,basename='StudentAddressview')
routers.register(r'all_student',AllStudentS,basename='all_student')

urlpatterns = [
    path('',include(routers.urls)),
    path('send-otp/',SendOtp.as_view()),
    
]

