# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_auto_20150508_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationinfo',
            name='creator_id',
            field=models.IntegerField(null=True),
        ),
    ]
