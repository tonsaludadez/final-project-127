# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('classyear', models.DecimalField(decimal_places=0, max_digits=4, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'class',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('donationno', models.DecimalField(decimal_places=0, max_digits=12, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True)),
                ('paymethod', models.CharField(blank=True, max_length=1, null=True)),
                ('installments', models.IntegerField(blank=True, null=True)),
                ('pledge_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'donation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('donorid', models.DecimalField(decimal_places=0, max_digits=9, primary_key=True, serialize=False)),
                ('fname', models.CharField(blank=True, max_length=30, null=True)),
                ('mname', models.CharField(blank=True, max_length=30, null=True)),
                ('lname', models.CharField(blank=True, max_length=30, null=True)),
                ('contactno', models.CharField(blank=True, max_length=12, null=True)),
                ('creditno', models.DecimalField(blank=True, decimal_places=0, max_digits=16, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'donor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EventDonation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'event_donation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('eventid', models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
                ('event_name', models.CharField(blank=True, max_length=30, null=True)),
                ('event_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'events',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transactionid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('date_paid', models.DateField(blank=True, null=True)),
                ('time_paid', models.TimeField(blank=True, null=True)),
                ('amount_paid', models.DecimalField(blank=True, decimal_places=2, max_digits=13, null=True)),
            ],
            options={
                'db_table': 'transaction',
                'managed': False,
            },
        ),
    ]
