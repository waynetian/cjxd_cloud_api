# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbaseinfo',
            name='domain_id',
            field=models.IntegerField(default=16),
            preserve_default=False,
        ),
    ]
