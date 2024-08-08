from django.contrib import admin
from myschool.models import Classes, StudentAddress,Teacher,Student,Task,ClassTask
# Register your models here.
@admin.register(Classes)
class Classes(admin.ModelAdmin):
    list_display=['title','slug']
    prepopulated_fields = {'slug':['title']}
    
@admin.register(Teacher)
class Teacher(admin.ModelAdmin):
    list_display=('id','first_name','last_name')

@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display=('id','first_name','last_name')
    
@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display=('id','title','status',"teacher_assigned","class_assigned")

@admin.register(ClassTask)
class ClassTask(admin.ModelAdmin):
    list_display=('id','status','task_id','student')
    
    
@admin.register(StudentAddress)
class StudentAddress(admin.ModelAdmin):
    list_display=('id','addresses','students')








# class ClassTaskAdmin(admin.ModelAdmin):
#     list_display = ('student', 'getmarks', 'remarks')

#     def remarks(self, obj):
#         if obj.getmarks > 30:
#             return 'Passed'
#         else:
#             return 'Failed'
#     remarks.short_description = 'Remarks'

# admin.site.register(ClassTask, ClassTaskAdmin)





