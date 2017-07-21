# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170721_0738'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['-date_modified']},
        ),
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['-date_modified']},
        ),
    ]
