# Generated by Django 2.2.17 on 2020-12-12 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20201212_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 12, 20, 43, 43, 724522), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 12, 20, 43, 43, 725521), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 12, 20, 43, 43, 727521), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='product',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 12, 12, 20, 43, 43, 726522), verbose_name='Опубликована'),
        ),
    ]
