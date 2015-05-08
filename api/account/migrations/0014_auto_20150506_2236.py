# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20150506_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbaseinfo',
            name='user',
            field=models.OneToOneField(related_name='user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
