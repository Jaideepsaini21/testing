# # # import jwt
# # # key="jai"
# # # token = jwt.encode({'id':'jaideep'},key,algorithm="HS256")
# # # print(token)

# # # decod = jwt.decode(token,key,algorithms="HS256")
# # # print(decod)
# # for i in range(5):
# #     if i==3:
# #         break
# #     print(i)
# # import jwt
# # from rest_framework.response import Response
# # from SDASchool.settings import SECRET_KEY
# # from django.contrib.auth.hashers import check_password
# # from rest_framework import status
# # from rest_framework.validators import ValidationError
# # from .models import Task, Teacher, Student, Classes
# # from myschool.serializers import TaskSerializers
# # from rest_framework.exceptions import AuthenticationFailed
# # def CheckIsAuthenticated(email, password, User, UserSerializer=None):
# #     user = User.objects.filter(email=email).first()
# #     if user:
# #         print('******', user)
# #         auth = check_password(password, user.password)
# #         print('auth', auth)
# #         if auth:
# #             encoded_jwt = jwt.encode({"id":user.id, "email":email}, SECRET_KEY, algorithm='HS256')
# #             print('encodedJWT', encoded_jwt)
# #             return Response({"token":encoded_jwt}, status=status.HTTP_200_OK)
# #         else:
# #             return Response({"error":"Invalid Password"}, status=status.HTTP_400_BAD_REQUEST)
# #     else:
# #             return Response({"error":"Invalid email"}, status=status.HTTP_400_BAD_REQUEST)
        

# # def decode(request, model, serial):
# #     data =  request.get('App-auth')
# #     print(data)
# #     if data:
# #         token = data.split(' ')
# #         print(token,"yes")
# #         print('token',token[0])
# #         if token[0].lower() == 'sjwt':
# #             try:
# #                 decoded = jwt.decode(token[1], SECRET_KEY, algorithms='HS256')
# #                 print('dict',decoded)
# #                 teacher=model.objects.filter(email=decoded["email"]).first()
# #                 print("teacher",teacher)
# #                 serializer=serial(teacher)
# #                 return Response(serializer.data)
                
# #             except:
# #                 raise ValidationError('Not Authenticated')
# #         else:
# #             return Response ({'error':"invalid token"},status=status.HTTP_400_BAD_REQUEST)

# #     else:
# #         return Response('Not Authenticated', status=status.HTTP_400_BAD_REQUEST)

    
#          student = Student.objects.get(id=student_id)
#         student_class = student.student_class
        
#         class_tasks = Task.objects.none()  # Start with an empty QuerySet
#         if student_class:
#         # Fetch tasks assigned to the student's class
#             class_tasks = Task.objects.filter(class_assigned=student_class)
        
#         # Fetch tasks assigned to the student directly
#         student_tasks = Task.objects.filter(student_assigned=student)
        
#         # Fetch tasks created by the student
#         created_tasks = Task.objects.filter(class_assigned=student)
        
#         # Combine all tasks, removing duplicates
#         all_tasks = class_tasks | student_tasks | created_tasks
#         return all_tasks.distinct()