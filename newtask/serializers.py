from rest_framework import serializers
from .models import Branch, Company, Employe

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
    
class EmployeSerializers(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField(method_name='get_employname')
    
    def get_employname(self,obj):
        data = Company.objects.filter(id=obj.branch.company_name.id).first()
        return data.name
    class Meta:
        model = Employe
        fields = "__all__"
        

class BranchSerializers(serializers.ModelSerializer): #branch me company ka name or empoy ki details aay
    company_name = serializers.CharField(read_only=True)
    employees = serializers.SerializerMethodField(method_name='get_employe')
    
    def get_employe(self,obj):
        data = Employe.objects.filter(branch=obj).values('name')
        # serializer=EmployeSerializers(data,many=True)
        return data       
    
    class Meta:
        model = Branch
        fields ="__all__"




        