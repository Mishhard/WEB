# Generated by Django 2.2.17 on 2021-06-14 22:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_auto_20210615_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 15, 1, 47, 35, 606418), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 15, 1, 47, 35, 609422), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 15, 1, 47, 35, 607417), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 15, 1, 47, 35, 610416), verbose_name='Дата'),
        ),
    ]
