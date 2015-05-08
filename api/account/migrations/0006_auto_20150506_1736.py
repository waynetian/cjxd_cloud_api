# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20150506_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='org',
            field=models.ManyToManyField(related_name='user_org', to='account.Organization'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.ManyToManyField(related_name='user_role', null=True, to='account.Role'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
