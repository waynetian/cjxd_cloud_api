# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=64)),
                ('note', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 't_business_type',
            },
        ),
        migrations.CreateModel(
            name='CompanyType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 't_company_type',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('short_name', models.CharField(max_length=64)),
                ('type', models.PositiveSmallIntegerField()),
                ('parent_id', models.IntegerField(default=0)),
                ('org_id_seq', models.CharField(default=b'/', max_length=512, null=True)),
                ('display_index', models.PositiveSmallIntegerField(default=32767, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 't_organization',
            },
        ),
        migrations.CreateModel(
            name='OrganizationInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('org_code', models.CharField(max_length=10)),
                ('stand_type', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=256)),
                ('certificate_number', models.CharField(max_length=30)),
                ('legal_person_id', models.CharField(max_length=18)),
                ('creator_id', models.IntegerField(null=True)),
                ('business_type_code', models.CharField(max_length=5)),
                ('business_tag', models.CharField(max_length=256)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('org', models.OneToOneField(to='account.Organization')),
            ],
            options={
                'db_table': 't_organization_info',
            },
        ),
        migrations.CreateModel(
            name='OrganizationToUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('parent_id', models.IntegerField(default=0)),
                ('job_type', models.PositiveSmallIntegerField(default=0)),
                ('job_title', models.CharField(default=None, max_length=32)),
                ('display_index', models.PositiveSmallIntegerField(default=32767, null=True)),
                ('status', models.PositiveSmallIntegerField(default=0)),
                ('org', models.ForeignKey(to='account.Organization')),
            ],
            options={
                'db_table': 't_organization_user',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.PositiveSmallIntegerField(serialize=False, primary_key=True)),
                ('role_name', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 't_role',
            },
        ),
        migrations.CreateModel(
            name='UserBaseInfo',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=32)),
                ('id_number', models.CharField(max_length=18, null=True)),
                ('email', models.EmailField(max_length=128)),
                ('email_act', models.BooleanField(default=False)),
                ('mobile_number', models.CharField(max_length=12, unique=True, null=True)),
                ('mobile_act', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 't_user_base_info',
            },
        ),
        migrations.AddField(
            model_name='organizationtouser',
            name='role',
            field=models.ForeignKey(to='account.Role'),
        ),
        migrations.AddField(
            model_name='organizationtouser',
            name='user',
            field=models.ForeignKey(to='account.UserBaseInfo'),
        ),
    ]
