# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20150505_1742'),
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
                ('parent_id', models.IntegerField()),
                ('org_id_seq', models.CharField(default=b'/', max_length=512)),
                ('display_index', models.PositiveSmallIntegerField(default=None)),
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
            name='Role',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('role_id', models.PositiveSmallIntegerField(default=0)),
                ('role_name', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 't_role',
            },
        ),
        migrations.CreateModel(
            name='UserBaseInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('id_number', models.CharField(max_length=18)),
                ('email', models.EmailField(max_length=64)),
                ('email_act', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 't_user_base_info',
            },
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={},
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_mobile',
            new_name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_login_time',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='parent_company_id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='person_id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='person_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_cert',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_email_act',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_mobile_act',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_state',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='display_index',
            field=models.PositiveSmallIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mobile_act',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='org_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='parent_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
