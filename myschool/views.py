from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from myschool.auth import CheckIsAuthenticated, decode
from myschool.permisions import IsTeacher,IsStudent
from myschool.serializers import ClassTaskSerializer, ClassesSerializers, MultipleAddressSerializer, StudentAddressSerializer,StudentAuthSerializer, StudentMarksSerializer,TeacherTaskAssigned,StudentTaskAssigned, TeacherAuthSerializer,ClassTask, TeacherSerializers, StudentSerializers, RegisterSerializers, TeacherValidationSerializer,StudentValidationSerializer,TaskSerializers, TechRegisterSerializers, TeacherSerializers
from myschool.models import Classes, Student, StudentAddress, Teacher,Task
from django.contrib.auth.hashers import make_password,check_password
from django.core.mail import send_mail
import random
from django.db.models import Q
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.validators import ValidationError
import jwt
from django.db.models import Sum
# Create your views here.
class ClassesViewset(ModelViewSet):
    queryset=Classes.objects.all()
    serializer_class = ClassesSerializers
    
class TeacherViewset(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TechRegisterSerializers
    http_method_names = ['get', 'post']
    
    def create(self, request, *args, **kwargs):
        email=request.data.get('email')
        password=request.data.get('password')
        otp=request.data.get('otp')
        hash=request.data.get('hash')
        
        if email and password and otp and hash:
            varification = check_password(otp,hash)
            if varification:
                return super().create(request, *args, **kwargs)
            else:
                return Response({"error:otp does not match"},status=status.HTTP_400_BAD_REQUEST)       
        else:
            return Response({"error: email,password,otp,hash are complasary"},status=status.HTTP_400_BAD_REQUEST)
        
        
    
    # def partial_update(self, request, *args, **kwargs):
    #     return super().partial_update(request, *args, **kwargs)
    
    # def get_queryset(self):
    #     return super().get_queryset()
    
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    
    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

 

class RegisterViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = RegisterSerializers
    http_method_names = ['post','get']
    
    def create(self, request, *args, **kwargs):
        otp = request.data.get('otp')
        password = request.data.get('password')
        hash = request.data.get('hash')
        email = request.data.get('email')
        if otp and password and hash and email:
            varification = check_password(otp,hash)
            if varification:
                return super().create(request, *args, **kwargs)
            else:
                return Response({'Error':'OTP Does Not Match'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Error':'otp,hash,password and email all fields are required'},status=status.HTTP_400_BAD_REQUEST)
            
   

class TeacherAuthViews(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherAuthSerializer
    http_method_names = ['post']
    
    def create(self, request):
        email = request.data.get('email')
        password= request.data.get('password')
        try:
            token = CheckIsAuthenticated(email, password, Teacher)
            return token
        except Exception as message:
            return Response({"error":message})
  
  
class StudentAuth(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentAuthSerializer
    http_method_names = ['post']      
    
    def create(self, request):
        email = request.data.get('email')
        password= request.data.get('password')
        try:
            token = CheckIsAuthenticated(email, password, Student)
            return token
        except Exception as message:
            return Response({"error":message})
    
    
    
        

class DecodeToken(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherValidationSerializer
    http_method_names = ['get']
    
    def list(self, request):
        print('response', request.headers)
        response = decode(request.headers, Teacher, TeacherValidationSerializer)
        
        if response.status_code == 200:
            user = response.data['id']
            data = Teacher.objects.get(id=user)
            serializer = TeacherValidationSerializer(data, many=False)
            return Response(serializer.data)
        else:
            return Response({'error':"not authorised"},status=status.HTTP_401_UNAUTHORIZED) 
  
    
class DecodeTokenS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentValidationSerializer
    http_method_names = ['get']
    
    def list(self, request):
        print('response', request.headers)
        response = decode(request.headers, Student, StudentValidationSerializer)
        
        if response.status_code == 200:
            user = response.data['id']
            print(user)
            data = Student.objects.get(id=user)
            serializer = StudentValidationSerializer(data, many=False)
            return Response(serializer.data)
        else:
            return Response({'error':"not authorised"},status=status.HTTP_401_UNAUTHORIZED)
   
 ## TASK ASSINED...
class TaskViewset(ModelViewSet):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializers
    http_method_names = ['post','get','patch','delete']
    permission_classes = [IsTeacher]
    
    def get_queryset(self):
        tescher_id = self.request.user_id
        print("JJJJJJJJJ",tescher_id)
        return Task.objects.filter(teacher_assigned_id=tescher_id)
    
    def get_serializer_context(self):
        return {"teacher":self.request.user_id}
    
class TeacherTask_Assigned(ModelViewSet):
    serializer_class = TeacherTaskAssigned
    http_method_names = ['get']
    permission_classes = [IsTeacher]
    
    def get_queryset(self):  # data show hoga jo ki is teacher na task diya ha students ko...
        teacher_id = self.request.user_id
        teacher_tasks = Task.objects.filter(teacher_assigned_id=teacher_id)
        return teacher_tasks
       

class StudentTask_Assigned(ModelViewSet): #task show hogy jo student ko mily ha complte.
    # queryset = Task.objects.all()
    serializer_class = StudentTaskAssigned
    http_method_names = ['get',"patch"]
    permission_classes = [IsStudent]
    
    def get_queryset(self):
        student_id = self.request.user_id 
        print("sssss",student_id)
        std_class=Student.objects.filter(id=student_id).first() 
            #and(,) or (|)
        classs=std_class.student_class #1 class me ha un k bi show hogy..
        student_tasks = Task.objects.filter(Q(class_assigned=classs))#classs
        # student_tasks = Task.objects.filter(Q(class_assigned=classs)|Q(student_assigned=std_class))#
        return student_tasks 

    
    
class ClassTaskViewset(ModelViewSet):
    # queryset = ClassTask.objects.all()
    serializer_class = ClassTaskSerializer
    http_method_names = ['get','patch']
    permission_classes = [IsTeacher]
    
    def get_queryset(self):
        class_id = self .request.user_id
        print("lllll",class_id)
        task = ClassTask.objects.filter(task_id__teacher_assigned=class_id)
        print("llllll",task)
        return task
        
    def get_serializer_context(self):
        return {"teacher":self.request.user_id}
    
  
from django.db.models import  Subquery, OuterRef, Sum, FloatField
class StudentMarksView(ModelViewSet):
    serializer_class = StudentMarksSerializer
    http_method_names = ['get','patch']
    permission_classes = [IsTeacher]
    
  
    def get_queryset(self):
        teacher_id = self.request.user_id
        print("lllll",teacher_id)

        # Subquery to calculate the final marks for each student
        final_marks_subquery = ClassTask.objects.filter(
            student=OuterRef('student'),
            status='C'
        ).values('student').annotate(
            total_marks=Sum('getmarks')
        ).values('total_marks')
        # print(final_marks_subquery,"[[[[[[[[[kkkk]]]]]]]]]")
        # Annotate the final marks and order by them
        task = ClassTask.objects.filter(
            task_id__teacher_assigned=teacher_id, status='C').annotate(
            final=Subquery(final_marks_subquery, output_field=FloatField())
        ).order_by('-final')

        return task
        
        # tea  = Teacher.objects.filter(id = teacher_id).first()
        # print("tea " , tea.teacher_class)
        # task=ClassTask.objects.filter(task_id__teacher_assigned=teacher_id,status='C')
    
        
        # teacher ki id jis sy us nay task diya ha wo.or complte ho gaya wo show hogi
    
 
class StudentAddressview(ModelViewSet):
    serializer_class = StudentAddressSerializer
    http_method_names = ['get']
    permission_classes = [IsStudent]
    
    def get_queryset(self):
        student_id = self.request.user_id 
        print("id",student_id)
        
        address = StudentAddress.objects.filter(students_id= student_id)
        print(address)
        return address
 
    

class AllStudentS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = MultipleAddressSerializer
    http_method_names = ['get']
     
    
    
           
      
       
         
         
    


     
#********************************************** APi Views ***************************************************#
def GenrateOtp():
    otp = random.randint(100000,999999)
    return otp

class SendOtp(APIView):
    def post(self,request):
        type = request.data.get('type')
        mail = request.data.get('email')
        print(mail)
                         #teacter
        if type == 'T':
            print(type)
            isTeacher = Teacher.objects.filter(email=mail).exists()
            if isTeacher:
                return Response({'error':'teacher already exist'})
            
            otp = GenrateOtp()
            try:
                send_mail(
                "otp teacher massage ",
                f"Your OTP  {otp}",
                "jaideeprda@gmail.com",
                ["jaideepsaini3460@gmail.com"],
                fail_silently=True,
            )
                print('mail send successfully')
            except Exception as msg:
                print('error',msg)
                pass
            hash = make_password(str(otp))
            print('1234567',hash)
            return Response({'msg':'OTP send successfully',"hesh":hash})
            
                       #student
        if type == 'S':
            print(type)
            isStudent = Student.objects.filter(email=mail).exists()
            if isStudent:
                return Response({'error':'student already exist'})
        
            
            otp = GenrateOtp()
            send_mail(
                " otp student massage ",
                f"Your OTP  {otp}",
                "jaideeprda@gmail.com",
                ["jaideepsaini3460@gmail.com"],
                fail_silently=True,
            )
            
            hash = make_password(str(otp))
            print('1234567',hash)
            return Response({'msg':'OTP send successfully',"hesh":hash})
            


# class StudentMarksView(APIView):
    
#     def get(self, request, class_id=None):
#         if class_id:
#             class_tasks = ClassTask.objects.filter(student__student_class_id=class_id)
#         else:
#             class_tasks = ClassTask.objects.all()
                
#         serializer = ClassTaskSerializer(class_tasks, many=True)
#         result = []    
#         for task in serializer.data:
#             student_name = f'{task["student"]["first_name"]} {task["student"]["last_name"]}'
#             marks = task['getmarks']
#             status = 'Pass' if marks >= 30 else 'Fail'
#             result.append({
#                 'student': student_name,
#                 'marks': marks,
#                 'status': status
#             })
                
#         return Response(result, status=status.HTTP_200_OK)
        
        
        





























            
            
        
          
        