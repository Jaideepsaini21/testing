from django.db import models

# Create your models here.
class Comman(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Company(Comman):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Branch(Comman):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    company_name = models.ForeignKey(Company,on_delete=models.CASCADE,blank=True,null=True,related_name="company_name")

    def __str__(self):
        return self.name
    
class Employe(Comman):
    name = models.CharField(max_length=100)
    employeid = models.IntegerField(default=0)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,blank=True,null=True,related_name="Employe")
    
    