# Generated by Django 2.2.17 on 2020-12-12 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20201212_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='qnt',
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 12, 20, 33, 15, 619690), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 12, 20, 33, 15, 622687), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 12, 20, 33, 15, 627685), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='product',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 12, 20, 33, 15, 626685), verbose_name='Опубликована'),
        ),
    ]
