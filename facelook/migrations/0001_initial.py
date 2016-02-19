# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=20)),
                ('user_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserMsg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('msg_title', models.CharField(max_length=200)),
                ('user_msg', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to='facelook.User')),
            ],
        ),
    ]
