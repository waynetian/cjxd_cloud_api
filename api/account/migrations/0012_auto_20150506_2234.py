# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_remove_userbaseinfo_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbaseinfo',
            old_name='user',
            new_name='user_id',
        ),
    ]
