# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20150506_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbaseinfo',
            name='email',
        ),
    ]
