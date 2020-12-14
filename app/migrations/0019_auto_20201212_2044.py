# Generated by Django 2.2.17 on 2020-12-12 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20201212_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 12, 20, 44, 25, 274012), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 12, 20, 44, 25, 275011), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 12, 20, 44, 25, 277009), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='product',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 12, 20, 44, 25, 276009), verbose_name='Опубликована'),
        ),
    ]