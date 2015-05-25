# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20150522_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbaseinfo',
            name='gender',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
