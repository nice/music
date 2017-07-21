# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 21, 1, 22, 55, 557438), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genre',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 21, 1, 23, 3, 837424), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 21, 1, 23, 25, 397376), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 21, 1, 23, 38, 933180), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='track',
            name='rating',
            field=models.IntegerField(default=1, choices=[(1, b'1 - Very Poor'), (2, b'2 - Poor'), (3, b'3 - Average'), (4, b'4 - Good'), (5, b'5 - Very Good')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='track',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
