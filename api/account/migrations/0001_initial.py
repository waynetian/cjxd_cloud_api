# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_name', models.CharField(max_length=32)),
                ('person_id', models.CharField(unique=True, max_length=18)),
                ('user_mobile', models.CharField(unique=True, max_length=12)),
                ('user_email', models.EmailField(max_length=64)),
                ('user_cert', models.CharField(default=0, max_length=1)),
                ('user_mobile_act', models.CharField(default=0, max_length=1)),
                ('user_email_act', models.CharField(default=0, max_length=1)),
                ('user_state', models.CharField(default=0, max_length=1)),
                ('parent_company_id', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('last_login_time', models.DateTimeField()),
            ],
            options={
                'verbose_name': 't_user_profile',
            },
        ),
    ]
