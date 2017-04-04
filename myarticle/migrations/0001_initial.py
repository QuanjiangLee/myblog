# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(blank=True, max_length=60)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-datetime'],
            },
        ),
    ]
