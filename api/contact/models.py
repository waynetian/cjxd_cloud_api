from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.contrib import admin

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    person_name = models.CharField(max_length=32, null=False)
    person_id = models.CharField(max_length=18, null=False, unique=True)
    user_mobile = models.CharField(max_length=12, null=False, unique=True)
    user_email = models.EmailField(max_length=64)
    user_cert = models.CharField(max_length=1, null=False, default=0)
    user_mobile_act = models.CharField(max_length=1, null=False, default=0)
    user_email_act = models.CharField(max_length=1, null=False, default=0)
    user_state = models.CharField(max_length=1, null=False, default=0)
    parent_company_id =  models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    last_login_time = models.DateTimeField(null=False) 


class UserRole(models.Model):
    user_role_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    role_id = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
 

class Role(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=64)
    role_note = models.CharField(max_length=256)


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=64)
    company_sname = models.CharField(max_length=20)
    organization_code = models.CharField(max_length=10)
    company_stand_type = models.CharField(max_length=10)
    company_address = models.CharField(max_length=256)
    certificate_number = models.CharField(max_length=30)
    parent_company_id = models.IntegerField()
    legal_person_id = models.IntegerField()
    business_type_code = models.CharField(max_length=5)
    business_tags = models.CharField(max_length=256)
    certification_state = models.CharField(max_length=1)
    company_state = models.CharField(max_length=1)
    refuse_reason = models.CharField(max_length=256)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
 


admin.site.register(UserProfile)
admin.site.register(UserRole)
admin.site.register(Role)
admin.site.register(Company)


