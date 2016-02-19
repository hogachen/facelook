# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_user_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermsg',
            name='msg_id',
            field=models.CharField(default=123, max_length=11),
            preserve_default=False,
        ),
    ]
