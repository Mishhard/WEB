# Generated by Django 2.2.17 on 2020-12-10 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201210_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 10, 20, 27, 48, 395751), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 10, 20, 27, 48, 398749), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 10, 20, 27, 48, 396750), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 10, 20, 27, 48, 399748), verbose_name='Дата'),
        ),
    ]
