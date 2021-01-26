# Generated by Django 3.1.5 on 2021-01-21 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shopsinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopename', models.CharField(max_length=32)),
                ('shopaddress', models.CharField(max_length=500)),
                ('processors', models.CharField(max_length=500)),
                ('motherboard', models.CharField(max_length=500)),
                ('ram', models.CharField(max_length=500)),
                ('gpu', models.CharField(max_length=500)),
                ('harddisk', models.CharField(max_length=500)),
                ('ssd', models.CharField(max_length=500)),
                ('casing', models.CharField(max_length=500)),
                ('processor_cooler', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='userinfos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=32)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user_cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop', models.CharField(max_length=500)),
                ('processors', models.CharField(max_length=500)),
                ('motherboard', models.CharField(max_length=500)),
                ('ram', models.CharField(max_length=500)),
                ('gpu', models.CharField(max_length=500)),
                ('harddisk', models.CharField(max_length=500)),
                ('ssd', models.CharField(max_length=500)),
                ('casing', models.CharField(max_length=500)),
                ('processor_cooler', models.CharField(max_length=500)),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pc_builder.shopsinfo')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pc_builder.userinfos')),
            ],
        ),
    ]
