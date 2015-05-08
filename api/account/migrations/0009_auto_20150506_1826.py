# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20150506_1740'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserToRole',
            new_name='RoleToUser',
        ),
        migrations.AlterModelTable(
            name='roletouser',
            table='t_role_user',
        ),
    ]
