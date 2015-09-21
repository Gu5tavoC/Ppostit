# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('printy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostItModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='postit',
            name='print_page',
            field=models.ForeignKey(related_name='posts', to='printy.PrintPage'),
        ),
        migrations.AddField(
            model_name='printpage',
            name='post_it_model',
            field=models.ForeignKey(default=1, to='printy.PostItModel'),
            preserve_default=False,
        ),
    ]
