# Generated by Django 3.1.5 on 2021-02-06 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_builder', '0003_user_cart_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
