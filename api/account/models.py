from django.contrib.auth.models import User
from django.contrib import admin

from django.db import models

# Create your models here.
class UserBaseInfo(models.Model):
    #id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, primary_key=True)
    name = models.CharField(max_length=32, null=False)
    id_number = models.CharField(max_length=18, null=True)
    email = models.EmailField(max_length=128, null=False)
    email_act = models.BooleanField(default=False)

    mobile_number = models.CharField(max_length=12, null=True, unique=True)
    mobile_act = models.BooleanField(default=False)
    gender = models.IntegerField(null=True, default=0)


    class Meta:
        db_table = 't_user_base_info'



class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False)
    short_name = models.CharField(max_length=64, null=False)
    type = models.PositiveSmallIntegerField(null=False)
    parent_id = models.IntegerField(null=False, default=0)
    org_id_seq = models.CharField(max_length=512,null=True,default='/')
    display_index = models.PositiveSmallIntegerField(null=True, default=32767)
    domain_id = models.IntegerField(null=False)

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 't_organization'


class OrganizationInfo(models.Model):
    id = models.AutoField(primary_key=True)
    org = models.OneToOneField(Organization)
    org_code = models.CharField(max_length=10)
    stand_type = models.CharField(max_length=10)
    address = models.CharField(max_length=256)
    certificate_number = models.CharField(max_length=30)
    legal_person_id = models.CharField(max_length=18)
    creator_id = models.IntegerField(null=True)
    business_type_code = models.CharField(max_length=5)
    business_tag = models.CharField(max_length=256)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 't_organization_info'


class Role(models.Model):
    role_id = models.PositiveSmallIntegerField(primary_key=True)
    role_name = models.CharField(max_length=32)
 
    class Meta:
        db_table = 't_role'


class OrganizationToUser(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserBaseInfo)
    org =  models.ForeignKey(Organization)
    role = models.ForeignKey(Role)
    
    parent_id = models.IntegerField(default=0)
    job_type = models.PositiveSmallIntegerField(default=0)
    job_title = models.CharField(max_length=32, default=None)
    display_index = models.PositiveSmallIntegerField(null=True, default=32767)
    status = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 't_organization_user'



class CompanyType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 't_company_type'


class BusinessType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    note = models.CharField(max_length=64)

    class Meta:
        db_table = 't_business_type'


