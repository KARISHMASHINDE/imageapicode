# Generated by Django 3.0.6 on 2020-05-05 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageprofile',
            name='Last_name',
            field=models.CharField(max_length=100),
        ),
    ]