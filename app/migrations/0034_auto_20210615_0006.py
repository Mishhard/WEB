# Generated by Django 2.2.17 on 2021-06-14 21:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_auto_20210614_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 15, 0, 6, 27, 714926), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 15, 0, 6, 27, 717925), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 15, 0, 6, 27, 715925), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 15, 0, 6, 27, 718919), verbose_name='Дата'),
        ),
    ]
