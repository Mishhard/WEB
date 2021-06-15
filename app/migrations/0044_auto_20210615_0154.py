# Generated by Django 2.2.17 on 2021-06-14 22:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_auto_20210615_0147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requisites',
            options={'ordering': ['-id'], 'verbose_name': 'Реквизиты', 'verbose_name_plural': 'Реквизиты'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 15, 1, 54, 22, 745729), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 15, 1, 54, 22, 747728), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 15, 1, 54, 22, 746728), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 6, 15, 1, 54, 22, 748727), verbose_name='Дата'),
        ),
    ]
