# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20150506_2236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbaseinfo',
            old_name='user',
            new_name='user_id',
        ),
    ]
