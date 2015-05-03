from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        #fields = ('user', 'person_name', 'person_id', 'user_mobile', \
        #          'user_email', 'parent_company_id', 'last_login_time')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company 
        fields = ('company_name', 'company_sname', 'organization_code', \
                  'company_stand_type', 'company_address', 'certificate_number',\
                  'legal_person_id', 'business_type_code', 'business_tags')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department


