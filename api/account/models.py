from django.contrib.auth.models import User
from django.contrib import admin

from django.db import models

# Create your models here.
class UserBaseInfo(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32, null=False)
    id_number = models.CharField(max_length=18, null=True)
    email_act = models.BooleanField(default=False)
    mobile_number = models.CharField(max_length=12, null=True, unique=True)
    mobile_act = models.BooleanField(default=False)
 
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

#class UserToOrganization(models.Model):
#    id = models.AutoField(primary_key=True)
#    user = models.ForeignKeyField(User)
#    org = models.ForeignKey(Organization)
#    relation = models.PositiveSmallIntegerField(default=0)
#    job_title = models.CharField(max_length=32)
#    create_time = models.DateTimeField(auto_now_add=True)
#    update_time = models.DateTimeField(auto_now=True)
#
#    class Meta:
#        db_table = 't_user_to_org'


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    role_id = models.PositiveSmallIntegerField(default=0)
    role_name = models.CharField(max_length=32)
 
    class Meta:
        db_table = 't_role'

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='user_profile') 
    #org = models.ManyToManyField(Organization, related_name='user_org')
    #job_type = models.PositiveSmallIntegerField(default=0)
    #job_title = models.CharField(max_length=32, default=None)
    #role = models.ManyToManyField(Role, related_name='user_role', null=False)
    parent_id = models.IntegerField(default=0)
    org_id = models.IntegerField(default=0)
    #display_index = models.PositiveSmallIntegerField(default=None)
    
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 't_user_profile'


class RoleToUser(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role)
    user = models.ForeignKey(User)
    org =  models.ForeignKey(Organization)

    class Meta:
        db_table = 't_role_user'

class OrganizationToUser(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    org =  models.ForeignKey(Organization)
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


