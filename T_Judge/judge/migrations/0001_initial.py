# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('deadline', models.DateTimeField(verbose_name='Deadline')),
                ('beginning', models.DateTimeField(verbose_name='Beginning')),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('definition', models.TextField(verbose_name='Definition')),
                ('homework', models.ForeignKey(to='judge.Homework')),
            ],
        ),
        migrations.CreateModel(
            name='Submit',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
                ('upload_date', models.DateTimeField(verbose_name='Upload Date', auto_now_add=True)),
                ('status', models.CharField(max_length=255, choices=[('Compilation Error', 'ce'), ('Wrong Answer', 'wr'), ('Runtime Error', 're'), ('Time Limit Exceeded', 'tl')], verbose_name='Status')),
                ('source_code', models.FileField(verbose_name='Source Code', upload_to='source_codes')),
                ('problem', models.ForeignKey(to='judge.Problem')),
            ],
        ),
    ]
