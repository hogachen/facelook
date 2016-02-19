# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_usermsg_msg_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermsg',
            name='msg_id',
        ),
    ]
