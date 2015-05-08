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
        fields = ('id', 'email')


class UserBaseInfoSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserBaseInfo
        fields = ('user', 'name', 'id_number', 'email_act') 

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        #fields = ('name', 'short_name', 'id', 'parent_id', 'type',\
        #          'display_index', '') 


class OrganizationInfoSerializer(serializers.ModelSerializer):
    org = OrganizationSerializer()

    class Meta:
        model = OrganizationInfo


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role

class RoleToUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleToUser


class CompanyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyType

class BusinessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessType







#class CompanySerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Company 
#        fields = ('company_name', 'company_sname', 'organization_code', \
#                  'company_stand_type', 'company_address', 'certificate_number',\
#                  'legal_person_id', 'business_type_code', 'business_tags')




#class DepartmentSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Department


