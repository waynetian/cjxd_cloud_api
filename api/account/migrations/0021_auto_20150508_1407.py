# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_organizationinfo_creator_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='mobile_act',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='mobile_number',
        ),
        migrations.AddField(
            model_name='userbaseinfo',
            name='mobile_act',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userbaseinfo',
            name='mobile_number',
            field=models.CharField(max_length=12, unique=True, null=True),
        ),
    ]
