# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20150506_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='display_index',
            field=models.PositiveSmallIntegerField(default=32767, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='org_id_seq',
            field=models.CharField(default=b'/', max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='parent_id',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
