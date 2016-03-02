# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_id', models.CharField(max_length=100)),
                ('zhi_user_id', models.CharField(max_length=100)),
                ('question_title', models.CharField(max_length=300)),
                ('insert_date', models.DateField()),
                ('upvote', models.IntegerField()),
                ('downvote', models.IntegerField()),
                ('zhi_answer_id', models.IntegerField()),
                ('zhi_answer_url', models.CharField(max_length=100)),
                ('zhi_upvote', models.IntegerField()),
                ('zhi_answer_content', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_id', models.CharField(max_length=100)),
                ('image_local_path', models.CharField(max_length=400)),
                ('image_url', models.CharField(max_length=400)),
                ('insert_date', models.DateField()),
                ('zhi_answer', models.ForeignKey(to='facelook.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=200)),
                ('tel', models.CharField(default=b'10086', max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserCollect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ForeignKey(to='facelook.Image')),
                ('user', models.ForeignKey(to='facelook.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserFavourite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ForeignKey(to='facelook.Image')),
                ('user', models.ForeignKey(to='facelook.User')),
            ],
        ),
        migrations.CreateModel(
            name='ZhiUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zhi_user_id', models.CharField(max_length=200)),
                ('user_url', models.CharField(max_length=300)),
                ('user_image', models.CharField(max_length=200)),
                ('sex', models.CharField(max_length=10, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab')),
                ('nickname', models.CharField(max_length=100, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
                ('short_introduce', models.CharField(max_length=200, verbose_name=b'\xe7\x9f\xad\xe4\xbb\x8b\xe7\xbb\x8d')),
                ('long_introduce', models.CharField(max_length=400, verbose_name=b'\xe9\x95\xbf\xe4\xbb\x8b\xe7\xbb\x8d')),
                ('sina', models.CharField(max_length=40, verbose_name=b'\xe6\x96\xb0\xe6\xb5\xaa\xe5\xbe\xae\xe5\x8d\x9a')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='zhi_user',
            field=models.ForeignKey(to='facelook.ZhiUser'),
        ),
    ]
