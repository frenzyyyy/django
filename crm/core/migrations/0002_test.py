# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-13 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Test_text', models.CharField(max_length=150)),
                ('Fi', models.CharField(max_length=50)),
            ],
        ),
    ]
