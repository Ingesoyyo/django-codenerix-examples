# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-22 11:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_auto_20170209_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('name', models.CharField(max_length=15, unique=True, verbose_name='Name')),
                ('symbol', models.CharField(max_length=2, unique=True, verbose_name='Symbol')),
                ('iso4217', models.CharField(max_length=3, unique=True, verbose_name='ISO 4217 Code')),
            ],
            options={
                'verbose_name': 'currency',
                'verbose_name_plural': 'currencies',
            },
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('cid', models.CharField(editable=False, max_length=128, unique=True, verbose_name='ID')),
                ('sell_amount', models.FloatField(verbose_name='Sell Amount')),
                ('buy_amount', models.FloatField(verbose_name='Buy Amount')),
                ('rate', models.FloatField(verbose_name='Rate')),
                ('buy_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exchanges_buy', to='base.Currency', verbose_name='Buy Currency')),
                ('owner', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL, verbose_name='Titular')),
                ('sell_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exchanges_sell', to='base.Currency', verbose_name='Sell Currency')),
            ],
            options={
                'verbose_name': 'exchange',
                'verbose_name_plural': 'exchanges',
            },
        ),
        migrations.RemoveField(
            model_name='contact',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='contactgroup',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='contactgroup',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='contact',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='ContactGroup',
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
    ]
