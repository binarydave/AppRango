# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
#from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('apprango', '0002_auto_20141204_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.datetime.now()),
            preserve_default=False,
        ),
    ]
