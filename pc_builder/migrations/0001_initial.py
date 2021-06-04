# Generated by Django 3.1.7 on 2021-06-03 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='com_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.CharField(max_length=150)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Shopsinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopename', models.CharField(default=False, max_length=32)),
                ('shopaddress', models.CharField(default=False, max_length=500)),
                ('shopimgaddress', models.CharField(default=False, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='userinfos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user_cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=500, null=True)),
                ('item_link', models.CharField(max_length=500)),
                ('quantity', models.IntegerField(default=1)),
                ('added_time', models.DateTimeField(auto_now_add=True)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pc_builder.shopsinfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pc_builder.userinfos')),
            ],
        ),
    ]
