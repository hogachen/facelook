# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_usermsg_msg_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermsg',
            name='msg_title',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
    ]
