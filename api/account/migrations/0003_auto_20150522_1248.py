# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userbaseinfo_domain_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbaseinfo',
            name='domain_id',
        ),
        migrations.AddField(
            model_name='organizationtouser',
            name='domain_id',
            field=models.IntegerField(default=54),
            preserve_default=False,
        ),
    ]
