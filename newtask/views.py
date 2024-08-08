from django.shortcuts import render
from .models import Branch, Company, Employe
from.serializers import BranchSerializers, CompanySerializers, EmployeSerializers 
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

# Create your views here.
class CompanyViewset(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
    http_method_names = ['get']
    
    

class BranchViewset(ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializers
    http_method_names = ['get']
    
    # def get_queryset(self):
    #     pass
    #     company_id = self.request.query_params.get('company_id')
    #     if company_id:
    #         return Branch.objects.filter(company_id=company_id)
    #     return Branch.objects.all()
    
class EmployeViewset(ModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializers
    http_method_names = ['get']





class Employeename(ModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializers
    http_method_names = ['get']
    