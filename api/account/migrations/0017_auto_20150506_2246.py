# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_auto_20150506_2245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbaseinfo',
            old_name='user_id',
            new_name='user',
        ),
    ]
