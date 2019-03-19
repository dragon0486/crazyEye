# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-11 04:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20180824_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('closed', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='host',
            name='system_type',
            field=models.CharField(choices=[('0', 'Windows'), ('1', 'Linux/Unix')], default='1', max_length=32),
        ),
        migrations.AlterField(
            model_name='hostgroup',
            name='host_to_remote_users',
            field=models.ManyToManyField(to='web.HostToRemoteUser'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='host_groups',
            field=models.ManyToManyField(blank=True, to='web.HostGroup'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='host_to_remote_users',
            field=models.ManyToManyField(blank=True, to='web.HostToRemoteUser'),
        ),
        migrations.AddField(
            model_name='auditlog',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.SessionTrack'),
        ),
    ]