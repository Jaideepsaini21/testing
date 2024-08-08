from django.contrib import admin
# from django.urls import path, include
from django.urls import include, path
from rest_framework import routers
from .views import BranchViewset, CompanyViewset, EmployeViewset, Employeename



routers = routers.DefaultRouter()
routers.register(r'Companies',CompanyViewset, basename='Companies')
routers.register(r'Branches',BranchViewset, basename='Branches')
routers.register(r'Employee',EmployeViewset, basename='Employee')

routers.register(r'Employname',Employeename, basename='Employname')


urlpatterns = [
    path('',include(routers.urls)),
    
   
]  