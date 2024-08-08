from rest_framework import serializers
from .models import StudentAddress, Teacher, Classes, Student, Task, ClassTask
from django.contrib.auth.hashers import make_password
from django.db.models import Sum

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields="__all__"
        
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"
        
class ClassesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Classes
        fields="__all__"
    
class RegisterSerializers(serializers.ModelSerializer):
    # otp = serializers.CharField(max_length=100)
    class Meta:
        model=Student
        fields="__all__"
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # password incrept from me mily ga
        return super().create(validated_data)

class TechRegisterSerializers(serializers.ModelSerializer):
    # otp = serializers.CharField(max_length=100)
    class Meta:
        model=Teacher
        fields="__all__"
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
           
class TeacherAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['email','password']

class TeacherValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields="__all__"
        
class StudentAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['email','password']

class StudentValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"
        

class TaskSerializers(serializers.ModelSerializer):
    
    # student_assigned = serializers.CharField(required=True) # filed are use required in post api does not reg.data
    class Meta:
        model=Task
        fields = '__all__'
        
    def create(self, valid_data):
        # sudent=valid_data.pop("student_assigned")
        # print(sudent,"pop")
        # student_instance=Student.objects.filter(id=sudent).first()
        # print("insasdasd",student_instance)
        teacher_data = self.context["teacher"]
        classp = valid_data["class_assigned"]
        print("class_id",classp)
        classstudent = Student.objects.filter(student_class_id=classp.id)
        print("kkkkkkkkkkkk",classstudent)
        task = Task.objects.create(teacher_assigned_id=teacher_data,**valid_data)
        print("TTTTT",task)
        for student in classstudent: # loop sy ha hum sabi student ko task de ry ha.1-by-1..
            ClassTask.objects.create(student=student,task_id=task) 
            # return task 
        # ClassTask.objects.create(title=valid_data["title"],task_id=task) # is me class task show hogy..
        return task
    
     
 
class TeacherTaskAssigned(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"
    

class StudentTaskAssigned(serializers.ModelSerializer):
    # teacher_assigned=serializers.CharField(read_only=True)
    class Meta:
        model=Task
        fields="__all__"
        
        
class ClassTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassTask
        fields = "__all__"


class StudentMarksSerializer(serializers.ModelSerializer):
    student=serializers.CharField(read_only=True)
    remarks = serializers.SerializerMethodField() #pass fail
    final = serializers.SerializerMethodField()#final marks in totalmarks me sy
    totalmarks = serializers.SerializerMethodField() #totalmarks
    # final_marks = serializers.IntegerField(read_only=True) 
    class Meta:
        model = ClassTask
        fields = "__all__"

    def get_remarks(self,obj):
        var =  ClassTask.objects.filter(student =obj.student,status='C')
       
        total=0
        for i in var:
            total=total+i.getmarks  # pass fail show.
        if(total>50):
            return 'Passed'
        else:
            return 'Failed'
        
    def get_final(self,obj): # all marks student show in another totalmarks me sy
        var =  ClassTask.objects.filter(student =obj.student,status='C')
       
        # total=sum(i.getmarks for i in var)
        total = 0
        for i in var:
            total=total+i.getmarks
        return total
    
    def get_totalmarks(self,obj):   # out of final marks in per students..
        var1 =  ClassTask.objects.filter(student =obj.student,status='C')
        final = 0
        for i in var1:
            final = final+i.task_id.marks
        return final
            

           
  
  
                   
        
class StudentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentAddress
        fields="__all__"

class MultipleAddressSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields="__all__"
        
    def get_address(self,obj):
        all_address=StudentAddress.objects.filter(students = obj).values("addresses")
        print(all_address,"sssssssss")
        return all_address
        
        
        
        
        
        
    

   
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    # def get_allmarks(self,obj):
    #     var =  ClassTask.objects.filter(student =obj.student,status='C').aggregate(Sum('getmarks'))
    #     print(var,"[[[[[ooo]]]]]")
    #     return var["getmarks__sum"]
        