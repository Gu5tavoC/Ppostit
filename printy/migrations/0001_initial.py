# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PostIt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=12)),
                ('body', models.CharField(max_length=512)),
                ('outside_code', models.CharField(max_length=32, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrintPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page', models.ForeignKey(to='printy.Page')),
            ],
        ),
        migrations.AddField(
            model_name='postit',
            name='print_page',
            field=models.ForeignKey(to='printy.PrintPage'),
        ),
    ]
