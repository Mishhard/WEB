# Generated by Django 2.2.17 on 2020-12-12 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20201212_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 12, 20, 31, 34, 638637), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 12, 20, 31, 34, 639638), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 12, 20, 31, 34, 641636), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='product',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 12, 20, 31, 34, 640637), verbose_name='Опубликована'),
        ),
    ]
