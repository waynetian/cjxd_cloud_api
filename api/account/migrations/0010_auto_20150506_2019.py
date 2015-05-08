# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20150506_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbaseinfo',
            name='id_number',
            field=models.CharField(max_length=18, null=True),
        ),
    ]
