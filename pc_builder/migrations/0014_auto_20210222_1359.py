# Generated by Django 3.1.5 on 2021-02-22 07:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_builder', '0013_auto_20210222_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopsinfo',
            name='addedtime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]