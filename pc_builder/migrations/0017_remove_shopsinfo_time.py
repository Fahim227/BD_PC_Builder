# Generated by Django 3.1.5 on 2021-02-22 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pc_builder', '0016_shopsinfo_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopsinfo',
            name='time',
        ),
    ]
