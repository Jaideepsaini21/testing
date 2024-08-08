from rest_framework.permissions import BasePermission
from .models import Teacher,Student
from .serializers import TeacherSerializers,StudentSerializers
from myschool.auth import decode

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        auth = decode(request.headers, Teacher, TeacherSerializers)
        if auth.status_code == 200:
            request.user_id = auth.data['id']
            return True
        else:
            False
            
class IsStudent(BasePermission):
    def has_permission(self, request, view):
        auth = decode(request.headers, Student, StudentSerializers)
        if auth.status_code == 200:
            request.user_id = auth.data['id']
            return True
        else:
            False