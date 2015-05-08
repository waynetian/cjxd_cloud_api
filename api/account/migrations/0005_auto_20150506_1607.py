# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='job_title',
            field=models.CharField(default=None, max_length=32),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='job_type',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='org',
            field=models.ManyToManyField(to='account.Organization'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.ManyToManyField(to='account.Role'),
        ),
    ]
