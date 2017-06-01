# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-01 02:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rodeos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityM',
            fields=[
                ('activity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actividades.Activity')),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Muerte de Animal',
                'verbose_name_plural': 'Muerte de Animales',
            },
            bases=('actividades.activity',),
        ),
        migrations.CreateModel(
            name='ActivityMovement',
            fields=[
                ('activity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='actividades.Activity')),
                ('cantidad', models.IntegerField()),
                ('stock_destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_destino', to='rodeos.Stock')),
            ],
            options={
                'verbose_name': 'Transferencia de Animal',
                'verbose_name_plural': 'Transferencia de Animales',
            },
            bases=('actividades.activity',),
        ),
        migrations.AddField(
            model_name='activity',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rodeos.Stock'),
        ),
    ]
