# Generated by Django 2.2.17 on 2021-06-14 22:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_auto_20210615_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 15, 1, 37, 16, 331942), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 15, 1, 37, 16, 335938), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 15, 1, 37, 16, 333940), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 15, 1, 37, 16, 336938), verbose_name='Дата'),
        ),
        migrations.AlterModelTable(
            name='requisites',
            table='requisites',
        ),
    ]
