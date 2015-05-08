# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0007_auto_20150506_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToRole',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('org', models.ForeignKey(to='account.Organization')),
                ('role', models.ForeignKey(to='account.Role')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 't_to_role',
            },
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='role',
        ),
    ]
