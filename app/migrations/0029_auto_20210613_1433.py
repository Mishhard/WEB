# Generated by Django 2.2.17 on 2021-06-13 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20210613_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 13, 14, 33, 3, 725480), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 13, 14, 33, 3, 727479), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 13, 14, 33, 3, 726480), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 13, 14, 33, 3, 728483), verbose_name='Дата'),
        ),
    ]
