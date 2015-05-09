# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_auto_20150507_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='parent_id',
            field=models.IntegerField(default=0),
        ),
    ]
