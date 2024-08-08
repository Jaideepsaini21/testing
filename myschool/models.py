from django.db import models
from django.contrib.auth.hashers import make_password,check_password 

# Create your models here.
class Comman(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Classes(Comman):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self) -> str:  # class name show nay hogi srif 1,2 show hoga..
        return self.title

class Teacher(Comman):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True,null=True)
    password = models.TextField()
    age = models.PositiveIntegerField(blank=True,null=True)
    dob = models.DateField(blank=True,null=True)
    teacher_class = models.ManyToManyField(Classes,related_name='class_teacher',db_index=True)
    
    def __str__(self) -> str:
        return self.first_name+" "+self.last_name
    
    
class Student(Comman):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True,null=True)
    password = models.TextField()
    age = models.PositiveIntegerField(blank=True,null=True)
    dob = models.DateField(blank=True,null=True)
    student_class = models.ForeignKey(Classes,on_delete=models.SET_NULL,blank=True,null=True,related_name='class_student',db_index=True)
    
    def __str__(self) -> str:
        return self.first_name+" "+self.last_name

    
class Task(Comman):
    title = models.CharField(max_length=100)
    COMPLETE = 'C'
    NOT_COMPLETE = 'NC'
    PENDING = 'P'
    IN_PROGRESS = 'IP'
    choice = [
        (COMPLETE,'Complete'),
        (NOT_COMPLETE,'Not Complete'),
        (PENDING,'Pending'),
        (IN_PROGRESS,'In Progress'),
        ]
    status = models.CharField(max_length=2,choices=choice,default='P')
    teacher_assigned = models.ForeignKey(Teacher,blank=True,on_delete=models.CASCADE,null = True,related_name='teacher_assigned')
    class_assigned = models.ForeignKey(Classes,blank=True,on_delete=models.CASCADE,null = True,related_name='class_assigned')
    marks = models.PositiveIntegerField(default=0)
    
    
    def __str__(self) -> str:
        return self.title


class ClassTask(models.Model):
    choice = [
        ('C','Complete'),
        ('NC','Not Complete'),
        ('P','Pending'),    
        ('IP','In Progress'),
    ]
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(max_length=2,choices=choice,default='P')
    task_id = models.ForeignKey(Task,on_delete=models.CASCADE,blank=True, null=True,related_name='task_id')
    getmarks = models.PositiveIntegerField(default=0)
    

class StudentAddress(Comman):
    addresses = models.TextField()
    students = models.ForeignKey(Student,on_delete=models.CASCADE,null=True,blank=True,related_name="StudentAddress")
    
    def __str__(self) -> str:
        return self.addresses
    
    
    



   
 









