from django.contrib import admin
from newtask.models import Company,Branch,Employe

# Register your models here.
@admin.register(Company)
class Company(admin.ModelAdmin):
    list_display=['name']
    
@admin.register(Branch)
class Branch(admin.ModelAdmin):
    list_display=['name','city','company_name']
    
@admin.register(Employe)
class Employe(admin.ModelAdmin):
    list_display=['name','employeid','branch']